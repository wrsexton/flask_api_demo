import time

def main(args):
    while True:
        print("hello " + args[0] if len(args) else "balls")
        time.sleep(3)

if __name__ == "__main__":
    main()