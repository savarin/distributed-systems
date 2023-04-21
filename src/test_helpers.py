import helpers


def test_encode_items():
    assert helpers.encode_item(None) == ""
    assert helpers.encode_item("") == "0:"
    assert helpers.encode_item([]) == "le"
    assert helpers.encode_item({}) == "de"

    assert helpers.encode_item(1) == "i1e"
    assert helpers.encode_item(-1) == "i-1e"
    assert helpers.encode_item(0) == "i0e"
    assert helpers.encode_item("foo") == "3:foo"

    assert helpers.encode_item([1]) == "li1ee"
    assert helpers.encode_item(["foo"]) == "l3:fooe"
    assert helpers.encode_item([1, "foo"]) == "li1e3:fooe"
    assert helpers.encode_item({"foo": 1}) == "d3:fooi1ee"

    assert helpers.encode_item([1, ["foo"]]) == "li1el3:fooee"
    assert helpers.encode_item({"foo": [1]}) == "d3:fooli1eee"
    assert helpers.encode_item([{"foo": 1}]) == "ld3:fooi1eee"
    assert helpers.encode_item({"foo": {"bar": "baz"}}) == "d3:food3:bar3:bazee"
