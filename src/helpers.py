from typing import Union
import builtins


Item = Union[int, str, list, dict]


def encode_item(item: Item) -> str:
    if item is None:
        return ""

    match type(item):
        case builtins.int:
            return f"i{str(item)}e"

        case builtins.str:
            assert isinstance(item, str)
            return f"{len(item)}:{item}"

        case builtins.list:
            assert isinstance(item, list)
            contents = "".join([encode_item(element) for element in item])
            return f"l{contents}e"

        case builtins.dict:
            assert isinstance(item, dict)
            elements: list[Item] = []

            for pair in sorted(item.items()):
                for element in pair:
                    elements.append(element)

            contents = "".join([encode_item(element) for element in elements])
            return f"d{contents}e"

        case _:
            raise Exception(f"Exhaustive switch error in encoding {item}.")
