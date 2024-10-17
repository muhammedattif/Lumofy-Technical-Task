# Python Standard Library Imports
from dataclasses import dataclass


@dataclass
class GeneralCodes:
    PREFIX = "GE"

    SUCCESS: str = PREFIX + "0"
    INVALID_DATA: str = PREFIX + "1"
    NOT_FOUND: str = PREFIX + "2"


@dataclass
class UploadedFilesCodes:
    PREFIX = "UF"

    INVALID_FILE: str = PREFIX + "0"


@dataclass
class CoursesCodes:
    PREFIX = "CO"

    INVALID_NAME: str = PREFIX + "0"
    INVALID_DESCRIPTION: str = PREFIX + "1"
    NOT_ENROLED: str = PREFIX + "2"


@dataclass
class LessonsCodes:
    PREFIX = "LE"

    INVALID_NAME: str = PREFIX + "0"
    INVALID_DESCRIPTION: str = PREFIX + "1"
    INVALID_CONTENT: str = PREFIX + "2"
