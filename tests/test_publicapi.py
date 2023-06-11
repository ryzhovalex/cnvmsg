def test_import():
    """
    Public API imports should be accessible by importing directly from the
    package.
    """
    from cnvmsg import (ConventionalMessage,  # noqa: I001, F401
                        MessageCondition,
                        MessageModule, MessageProject,
                        MessageStatus, MessageType,
                        parse)
