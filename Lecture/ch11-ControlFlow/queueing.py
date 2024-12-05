#!/usr/bin/env python3
# asyncq.py

import asyncio
import itertools as it
import os
import random
import time
import argparse

async def makeitem(size: int = 5) -> str:
    """
    랜덤한 바이너리 데이터를 생성하고 이를 16진수 문자열로 반환합니다.

    Args:
        size (int): 생성할 랜덤 바이너리 데이터의 크기(바이트 단위). 기본값은 5.

    Returns:
        str: 16진수로 인코딩된 랜덤 데이터 문자열.

    Note:
        데이터는 보안적으로 안전한 랜덤 데이터로 생성됩니다.
    """
    return os.urandom(size).hex()


async def randsleep(caller=None) -> None:
    """
    랜덤한 시간 동안 비동기적으로 대기합니다.

    Args:
        caller (str, optional): 호출자의 이름이나 정보를 출력하는 데 사용됩니다. 
                                기본값은 None.

    Note:
        대기 시간은 0에서 10초 사이의 랜덤 값으로 설정됩니다.
        호출자 정보가 제공되면 대기 시간과 호출자 정보를 출력합니다.
    """
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue) -> None:
    """
    생산자 역할을 하는 비동기 함수로, 데이터를 생성하여 큐에 추가합니다.

    1. 랜덤한 수의 아이템을 생성합니다.
    2. 각 아이템마다 랜덤 시간 동안 대기합니다.
    3. 아이템을 생성하고 큐에 추가합니다.

    Args:
        name (int): 생산자를 구분하는 식별자.
        q (asyncio.Queue): 소비자와 데이터를 공유하는 비동기 큐.

    Note:
        각 생산자는 랜덤한 횟수만큼 아이템을 생성하며, 
        각 아이템 생성 시 랜덤 대기 시간을 가집니다.
    """
    n = random.randint(1, 5)  # 생성할 아이템 수를 랜덤하게 설정
    print(f"Producer {name}, items : {n}")
    for _ in it.repeat(None, n):  # n번 반복
        await randsleep(caller=f"Producer {name}")  # 랜덤 시간 대기
        i = await makeitem()  # 랜덤 데이터 생성
        t = time.perf_counter()  # 현재 시간 기록
        await q.put((i, t))  # 큐에 데이터와 생성 시간 추가
        print(f"Producer {name} added <{i}> to queue.")


async def consume(name: int, q: asyncio.Queue) -> None:
    """
    소비자 역할을 하는 비동기 함수로, 큐에서 데이터를 가져와 처리합니다.
    무한 루프를 실행하며, 큐에 데이터가 들어올 때까지 대기합니다.

    1. 랜덤 시간 동안 대기합니다.
    2. 큐에서 데이터를 가져옵니다.
    3. 데이터를 처리하며 처리 시간을 출력합니다.
    4. 작업 완료를 큐에 알립니다.

    Args:
        name (int): 소비자를 구분하는 식별자.
        q (asyncio.Queue): 생산자와 데이터를 공유하는 비동기 큐.

    Note:
        이 함수는 무한 루프를 실행하며, 큐에 데이터가 추가되기를 계속 기다립니다.
        태스크 취소(`task.cancel()`)가 호출되어야 종료됩니다.
    """
    while True:
        await randsleep(caller=f"Consumer {name}")  # 랜덤 시간 대기
        i, t = await q.get()  # 큐에서 데이터 가져오기
        now = time.perf_counter()  # 현재 시간 기록
        print(f"Consumer {name} got element <{i}>"
              f" in {now-t:0.5f} seconds.")  # 처리 시간 출력
        q.task_done()  # 큐 작업 완료 알림


async def main(nprod: int, ncon: int) -> None:
    """
    생산자-소비자 패턴을 비동기적으로 실행합니다.
    
    1. 공유 큐 (`asyncio.Queue`)를 생성합니다.
    2. 지정된 수만큼 생산자와 소비자 태스크를 생성합니다.
    3. 생산자 태스크를 실행하고 완료될 때까지 기다립니다.
    4. 큐에 남은 모든 작업이 처리될 때까지 대기합니다.
    5. 소비자 태스크를 취소하여 종료합니다.

    Args:
        nprod (int): 생성할 생산자 태스크의 수
        ncon (int): 생성할 소비자 태스크의 수

    Note:
        생산자와 소비자의 수를 매개변수로 조정하여 비동기 처리 성능을 실험할 수 있습니다.
    """
    q = asyncio.Queue()  # 공유 큐 생성
    print(nprod, ncon)
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]  # 생산자 태스크 생성
    print(producers)
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]  # 소비자 태스크 생성
    await asyncio.gather(*producers)  # 모든 생산자 태스크 실행 및 완료 대기
    await q.join()  # 큐의 모든 작업이 완료될 때까지 대기
    for c in consumers:  # 소비자 태스크 취소
        c.cancel()


if __name__ == "__main__":
    """
    프로그램 진입점으로, 비동기 main 함수 실행과 실행 시간 측정을 담당합니다.
    """
    # pydoc queueing 으로 docstring의 내용을 볼수 있다.
    # Random seed 설정 및 시간 측정
    random.seed(time.time())    
    start = time.perf_counter()
    asyncio.run(main(3, 2))  # main 함수 실행 (생산자 3명, 소비자 2명)
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")  # 실행 시간 출력