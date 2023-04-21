import helpers


def test_encode_item():
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


def test_decode_item():
    assert helpers.decode_item("") == None
    assert helpers.decode_item("0:") == ""
    assert helpers.decode_item("le") == []
    assert helpers.decode_item("de") == {}
    assert helpers.decode_item("i1e") == 1
    assert helpers.decode_item("i-1e") == -1
    assert helpers.decode_item("i0e") == 0
    assert helpers.decode_item("3:foo") == "foo"
    assert helpers.decode_item("li1ee") == [1]
    assert helpers.decode_item("l3:fooe") == ["foo"]
    assert helpers.decode_item("li1e3:fooe") == [1, "foo"]
    assert helpers.decode_item("d3:fooi1ee") == {"foo": 1}
    assert helpers.decode_item("li1el3:fooee") == [1, ["foo"]]
    assert helpers.decode_item("d3:fooli1eee") == {"foo": [1]}
    assert helpers.decode_item("ld3:fooi1eee") == [{"foo": 1}]
    assert helpers.decode_item("d3:food3:bar3:bazee") == {"foo": {"bar": "baz"}}
