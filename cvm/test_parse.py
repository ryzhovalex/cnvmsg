from cvm.parse import parse


def test_main():
    inp: str = \
        r"%after completing #1% [waiting] ussr/feat: ability to call a" \
        r" comrad #community #pyatiletka"

    parse(inp)

    assert 0, "OK"
