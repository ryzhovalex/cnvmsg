from pydantic import BaseModel

from cvm.enums import CvmStatus, CvmType
from cvm.errors import MissingFieldError


class CvmCondition(BaseModel):
    text: str


class CvmProject(BaseModel):
    name: str


class CvmModule(BaseModel):
    name: str


class Cvm(BaseModel):
    """
    Main conventional message represenation model.
    """
    message: str
    condition: CvmCondition | None = None
    status: CvmStatus | None = None
    project: CvmProject | None = None
    type: CvmType | None = None
    module: CvmModule | None = None
    is_breaking: bool = False
    text: str
    tags: list[str] | None = None

    @property
    def condition_text(self) -> str:
        if self.condition is None:
            raise MissingFieldError(field="condition")
        else:
            return self.condition.text

    @property
    def status_text(self) -> str:
        if self.status is None:
            raise MissingFieldError(field="status")
        else:
            return self.status.value

    @property
    def project_text(self) -> str:
        if self.project is None:
            raise MissingFieldError(field="project")
        else:
            return self.project.name

    @property
    def type_text(self) -> str:
        if self.type is None:
            raise MissingFieldError(field="type")
        else:
            return self.type.value

    @property
    def module_text(self) -> str:
        if self.module is None:
            raise MissingFieldError(field="module")
        else:
            return self.module.name
