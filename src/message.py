import dataclasses

import helpers


@dataclasses.dataclass
class Message:
    source: int
    target: int
    text: str


def encode_message(message: Message) -> str:
    attributes = vars(message).copy()
    return helpers.encode_item(attributes)


def decode_message(string: str) -> Message:
    attributes = helpers.decode_item(string)
    assert isinstance(attributes, dict)
    return Message(**attributes)
