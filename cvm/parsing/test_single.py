from pprint import pprint
from cvm.models import Cvm
from cvm.parsing._parse import parse


def test_condition():
    inp: str = r"%after lunch% ability to call a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition_text == "after lunch"
    assert cvm.status is None
    assert cvm.project is None
    assert cvm.type is None
    assert cvm.module is None
    assert cvm.is_breaking == False
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None


def test_status():
    inp: str = r"[waiting] ability to call a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status_text == "waiting"
    assert cvm.project is None
    assert cvm.type is None
    assert cvm.module is None
    assert cvm.is_breaking == False
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None


def test_text():
    inp: str = "ability to call a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project is None
    assert cvm.type is None
    assert cvm.module is None
    assert cvm.is_breaking == False
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None


def test_redundant_spaces_text():
    inp: str = "ability      to             call        a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project is None
    assert cvm.type is None
    assert cvm.module is None
    assert cvm.is_breaking == False
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None


def test_tags():
    inp: str = "ability to call a comrad #community #pyatiletka"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project is None
    assert cvm.type is None
    assert cvm.module is None
    assert cvm.is_breaking == False
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags == ["community", "pyatiletka"]


def test_stranded_tags():
    inp: str = "ability #forall to call a comrad #community #pyatiletka"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project is None
    assert cvm.type is None
    assert cvm.module is None
    assert cvm.is_breaking == False
    # the redundant spaces should be correctly trimmed
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags == ["forall", "community", "pyatiletka"]


def test_breaking():
    inp: str = "!: ability to call a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project is None
    assert cvm.type is None
    assert cvm.module is None
    assert cvm.is_breaking == True
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None


def test_module():
    inp: str = "(factory): ability to call a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project is None
    assert cvm.type is None
    assert cvm.module_text == "factory"
    assert cvm.is_breaking == False
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None


def test_type():
    inp: str = "feat: ability to call a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project is None
    assert cvm.type_text == "feat"
    assert cvm.module is None
    assert cvm.is_breaking == False
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None


def test_project():
    inp: str = "ussr: ability to call a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project_text == "ussr"
    assert cvm.type is None
    assert cvm.module is None
    assert cvm.is_breaking == False
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None
