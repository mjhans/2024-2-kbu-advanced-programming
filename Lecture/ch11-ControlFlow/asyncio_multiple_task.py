import asyncio
import time
import random

async def random_sleep(num):
    rand = random.randint(1,10) # 1~10 사이의 랜덤한 정수
    print(f"{'*' * num} - {num}번 코루틴: {rand}초 동안 대기")
    await asyncio.sleep(rand) # time.sleep() 대신 asyncio.sleep() 사용
    #time.sleep(rand)
    print(f"{'*' * num} - {num}번 코루틴: {rand}초 이후 종료")
    return f"{rand}초"
    

async def main():
    tasks = [asyncio.create_task(random_sleep(idx)) 
             for idx in range(10)] # generator expression
    #tasks = (random_sleep(idx) for idx in range(10)) # generator expression
    
    # tasks[0],tasks[1],.....tasks[9]가 각각의 코루틴 객체
    tasks_results = await asyncio.gather(*tasks) 
    return tasks_results

result = asyncio.run(main())

print(f"{result = }")