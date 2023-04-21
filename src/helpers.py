from typing import Optional, Tuple, Union
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


def decode_item(string: str) -> Optional[Item]:
    def closure(string: str) -> Tuple[Optional[Item], str]:
        if string == "":
            return None, ""

        elif string[0].isdigit():
            counter = 1

            while string[counter].isdigit():
                counter += 1

            length = int(string[:counter])

            if length == 0:
                return "", ""

            assert string[counter] == ":"
            return (
                string[counter + 1 : counter + 1 + length],
                string[counter + 1 + length :],
            )

        elif string.startswith("i"):
            counter = 1

            if string[counter] == "-":
                counter += 1

            while string[counter].isdigit():
                counter += 1

            assert string[counter] == "e"
            return int(string[1:counter]), string[counter + 1 :]

        elif string[0] in {"l", "d"}:
            items = []
            rest = string[1:]

            while not rest.startswith("e"):
                item, rest = closure(rest)
                items.append(item)

            assert rest[0] == "e"
            rest = rest[1:]

            if string.startswith("l"):
                return items, rest

            return {k: v for k, v in zip(items[::2], items[1::2])}, rest

        else:
            raise Exception(f"Cannot decode {string}.")

    return closure(string)[0]
