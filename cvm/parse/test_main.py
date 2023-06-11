from pprint import pprint
from cvm.models import Cvm
from cvm.parse.parse import parse


def test_main():
    inp: str = \
        r"%after completing #1% [waiting] ussr/feat: ability to call a" \
        r" comrad #community #pyatiletka"

    cvm: Cvm = parse(inp)
    print()
    pprint(cvm.dict())

    assert 0, "OK"
