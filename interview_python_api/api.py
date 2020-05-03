from dataclasses import dataclass
from typing import List
import datetime

@dataclass
class Client:
    access_token_key:    str
    access_token_secret: str

    def list(self, object_name: str) -> List[str]:
        return ['a']*5

    def query(self, object_name: str, start_date: datetime, end_date: datetime) -> List[str]:
        return ['b']*10

