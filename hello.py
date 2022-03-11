import sys
import time

def main():
    args = sys.argv
    while True:
        print("hello " + args[1] if len(args) > 1 else "balls")
        time.sleep(3)


if __name__ == "__main__":
    main()