def test_import():
    """
    Public API imports should be accessible by importing directly from the
    package.
    """
    from cvm import (Cvm, CvmCondition, CvmModule,  # noqa: I001, F401
                     CvmProject, CvmStatus, CvmType, parse)
