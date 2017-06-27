#filename:sleeping_1:py
import time
import os

def main(cmd,inc=5):
    while True:
        os.system(cmd)
        time.sleep(inc)

s=main("nslookup www.qq.com",1)

