from typing import Dict, Optional
import dataclasses


@dataclasses.dataclass
class Application:
    def __post_init__(self) -> None:
        self.dictionary: Dict[str, str] = {}

    def set_value(self, key: str, value: str) -> None:
        self.dictionary[key] = value

    def get_value(self, key: str) -> Optional[str]:
        return self.dictionary.get(key, None)
