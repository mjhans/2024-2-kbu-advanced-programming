import aiohttp
import asyncio
import time

from download_flag import *

def big_save_flag(img, filename): 
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR, exist_ok=True) # 없으면 디렉토리 생성
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


async def async_get_flag(cc):
    url = f"{BASE_URL}/{cc.lower()}/{cc.lower()}.gif"
    async with aiohttp.request("GET", url) as resp:
        return await resp.read()

async def async_download_one(cc):
    loop = asyncio.get_running_loop() #실행중인 이벤트 루프를 갖고 온다. 
    semaphore = asyncio.Semaphore(10) # 동시에 3
    async with semaphore:
        image = await async_get_flag(cc)
        show(cc)
        
        loop.run_in_executor(None, big_save_flag, image, cc.lower() + ".gif")
        #big_save_flag(image, cc.lower() + ".gif")
        return cc

async def download_coro(cc_list):
    tasks = [asyncio.create_task(async_download_one(cc))
             for cc in sorted(cc_list)]
    return await asyncio.gather(*tasks)
    
    
def download_many(cc_list):
    return asyncio.run(download_coro(cc_list)) # 다수의 task를 등록하고 동시에 실행하는 코루틴을 실행
    
def main(download_many):
    t0 = time.time()
    res = download_many(POP20_CC)
    count = len(res)
    elapsed = time.time() - t0
    msg = f'\n {count} flags downloaded in {elapsed:.2f}s'
    print(msg)
    
if __name__ == '__main__':
    main(download_many)
    
    
    