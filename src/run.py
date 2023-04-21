import signal
import sys


def handler(sig, frame):
    print("Exit on Ctrl+C.")
    sys.exit(0)


if __name__ == "__main__":
    identifier = 0

    try:
        while True:
            prompt = input(f"{identifier} > ")

            if prompt in {"", "exit"}:
                break

            print(prompt)

    except KeyboardInterrupt:
        print("\nExit on SIGINT.")
        sys.exit(0)
