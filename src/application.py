from typing import Dict, Optional
import dataclasses

import helpers


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
