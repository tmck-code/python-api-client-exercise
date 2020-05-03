from typing import List, Optional
from enum import Enum
import random

from pydantic.dataclasses import dataclass

class RecordSaveError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

@dataclass
class PersonName:
    first_name:   str
    last_name:    str

class OptInStatus(Enum):
    OPT_OUT = 0
    OPT_IN  = 1

@dataclass
class Person:
    email: str
    name:  PersonName
    opt_in_status: OptInStatus

