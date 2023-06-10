from cvm.enums import CvmStatus, CvmType
from cvm.models import Cvm, CvmCondition, CvmModule, CvmProject


class _Blocks:
    def __init__(self) -> None:
        # states: 0=processed, 1=completed
        self._state_by_name: dict[str, int] = {}
        self._processed_name: str | None = None

    def start(self, name: str) -> None:
        if self._processed_name is not None:
            raise ValueError(
                f"cannot start name={name} when another"
                f" name is processed pname={self._processed_name}"
            )
        elif name in self._state_by_name:
            raise ValueError(f"cannot start already existing name={name}")
        self._state_by_name[name] = 0

    def latest(self) -> str | None:
        if len(self._arr) == 0:
            return None
        else:
            return self._arr[len(self._arr)-1]


def parse(message: str) -> Cvm:
    """
    Parses string into Conventional Message.
    """
    condition: CvmCondition | None = None
    status: CvmStatus | None = None
    project: CvmProject | None = None
    cvmtype: CvmType | None = None
    module: CvmModule | None = None
    is_breaking: bool = False
    text: str = ""
    tags: list[str] | None = None

    blocks: _Blocks = _Blocks()

    # iterate message manually to ensure perfectly correct message
    for i, c in enumerate(message):
        if c == "%":
            if blocks.latest is None:

    return Cvm(
        message=message,
        condition=condition,
        status=status,
        project=project,
        type=cvmtype,
        module=module,
        is_breaking=is_breaking,
        text=text,
        tags=tags
    )
