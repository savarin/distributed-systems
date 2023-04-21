import dataclasses

import application
import message
import node


@dataclasses.dataclass
class Server:
    identifier: int = 0

    def __post_init__(self) -> None:
        self.node: node.Node = node.Node(self.identifier)
        self.application: application.Application = application.Application()

    def respond(self) -> None:
        while True:
            payload = self.node.receive()

            try:
                request = message.decode_message(payload)
                print(f"{request.source} > {request.target} {payload}")

                response = self.application.handle_message(request)
                self.node.send(request.source, message.encode_message(response))

            except Exception as e:
                print(f"Exception: {e}")

    def run(self) -> None:
        self.node.start()
        self.respond()


if __name__ == "__main__":
    server = Server()
    server.run()
