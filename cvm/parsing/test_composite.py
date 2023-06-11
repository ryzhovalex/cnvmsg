from cvm.models import Cvm
from cvm.parsing._parse import parse


def test_project_type():
    inp: str = "ussr/feat: ability to call a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project_text == "ussr"
    assert cvm.type_text == "feat"
    assert cvm.module is None
    assert cvm.is_breaking == False
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None


def test_project_type_module():
    inp: str = "ussr/feat(factory): ability to call a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project_text == "ussr"
    assert cvm.type_text == "feat"
    assert cvm.module_text == "factory"
    assert cvm.is_breaking == False
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None


def test_project_type_module_breaking():
    inp: str = "ussr/feat(factory)!: ability to call a comrad"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition is None
    assert cvm.status is None
    assert cvm.project_text == "ussr"
    assert cvm.type_text == "feat"
    assert cvm.module_text == "factory"
    assert cvm.is_breaking == True
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags is None


def test_composite():
    inp: str = \
        r"%after lunch% [waiting] ussr/feat(factory)!: ability to" \
        " call a comrad #community #pyatiletka"

    cvm: Cvm = parse(inp)

    assert cvm.message == inp
    assert cvm.condition_text == "after lunch"
    assert cvm.status_text == "waiting"
    assert cvm.project_text == "ussr"
    assert cvm.type_text == "feat"
    assert cvm.module_text == "factory"
    assert cvm.is_breaking == True
    assert cvm.text == "ability to call a comrad"
    assert cvm.tags == ["community", "pyatiletka"]
