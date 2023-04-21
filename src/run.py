import sys

import application


def handler(sig, frame):
    print("Exit on Ctrl+C.")
    sys.exit(0)


if __name__ == "__main__":
    app = application.Application()
    identifier = 0

    try:
        while True:
            prompt = input(f"{identifier} > ")

            if prompt in {"", "exit"}:
                break

            elif prompt.startswith("set "):
                args = prompt[4:].split(" ")

                if len(args) != 2:
                    print(f"Invalid set command '{prompt}'.")
                    continue

                app.set_value(args[0], args[1])
                print(f"set {args[0]}: {args[1]}")

            elif prompt.startswith("get "):
                args = prompt[4:].split(" ")

                if len(prompt[4:].split(" ")) != 1:
                    print(f"Invalid get command '{prompt}'.")

                value = app.get_value(args[0])
                print(f"get {args[0]}: {value}")

            else:
                print(f"Invalid command '{prompt}'.")

    except KeyboardInterrupt:
        print("\nExit on SIGINT.")
        sys.exit(0)
