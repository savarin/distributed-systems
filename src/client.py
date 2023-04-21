import dataclasses
import sys

import message
import node


@dataclasses.dataclass
class Client:
    identifier: int

    def __post_init__(self) -> None:
        self.node: node.Node = node.Node(self.identifier)

    def instruct(self) -> None:
        while True:
            prompt = input(f"{self.identifier} > 0 ")

            if prompt in {"", "exit"}:
                return None

            request = message.Message(self.identifier, 0, prompt)
            self.node.send(0, message.encode_message(request))

            payload = self.node.receive()
            response = message.decode_message(payload)
            print(f"{request.source} > {request.target} {payload}")
            print(f"{response.text}")

    def run(self) -> None:
        self.node.start()
        self.instruct()


if __name__ == "__main__":
    client = Client(int(sys.argv[1]))
    client.run()
