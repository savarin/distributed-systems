from typing import Dict, Optional
import dataclasses

import helpers
import message


@dataclasses.dataclass
class Application:
    def __post_init__(self) -> None:
        self.dictionary: Dict[str, str] = {}

    def write_file(self, filename: str) -> None:
        with open(filename, "w") as f:
            contents = helpers.encode_item(self.dictionary)
            f.write(contents)

    def read_file(self, filename: str) -> None:
        with open(filename) as f:
            contents = helpers.decode_item(f.read())

            assert isinstance(contents, dict)
            self.dictionary = contents

    def set_value(self, key: str, value: str) -> None:
        self.dictionary[key] = value

    def get_value(self, key: str) -> Optional[str]:
        return self.dictionary.get(key, None)

    def handle_message(self, msg: message.Message) -> message.Message:
        args = msg.text.split(" ")

        if args[0] == "set":
            assert len(args) == 3
            self.set_value(args[1], args[2])

            return message.Message(msg.target, msg.source, "OK")

        elif args[0] == "get":
            assert len(args) == 2
            value = self.get_value(args[1]) or "nil"

            return message.Message(msg.target, msg.source, value)

        return message.Message(msg.target, msg.source, "error")
