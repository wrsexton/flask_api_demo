import sys
import time

def hello():
    args = sys.argv
    while True:
        print("hello " + args[1] if len(args) > 1 else "balls")
        time.sleep(3)