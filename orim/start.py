import imp
from multiprocessing import Process
import os
# 중략
def start_server():
    # 서버 실행
    print('Server Start.')
    os.system(f'python3 manage.py runserver')

def main2():
    # 무한반복 모듈 실행
    import time
    i = 0
    while True:
        i = i+1
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    Process(target=start_server).start()
    Process(target=main2).start()