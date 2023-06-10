from pydantic import BaseModel

from cvm.enums import CvmStatus, CvmType


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
