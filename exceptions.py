"""MEF Eline Exceptions."""


class MEFELineException(Exception):
    """MEF Eline Base Exception."""


class EVCException(MEFELineException):
    """EVC Exception."""


class ValidationException(EVCException):
    """Exception for validation errors."""


class FlowModException(MEFELineException):
    """Exception for FlowMod errors."""


class InvalidPath(MEFELineException):
    """Exception for invalid path."""


class DisabledSwitch(MEFELineException):
    """Exception for disabled switch in path"""


class DuplicatedNoTagUNI(Exception):
    """Exception for duplicated no TAG UNI"""
    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return f"DuplicatedNoTagUNI, {self.msg}"

    def __repr__(self) -> str:
        return f"DuplicatedNoTagUNI, {self.msg}"