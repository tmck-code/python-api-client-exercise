from dataclasses import dataclass
from typing import List, Iterator
from datetime import datetime

from python_api_client_exercise.underbelly import Underbelly

@dataclass
class APIObject:
    created_at: datetime
    identifier: str
    data:       dict

ENDPOINTS = ['lists', 'customers', 'products']

@dataclass
class Client:
    access_token_key:    str
    access_token_secret: str

    def fetch(self, endpoint: str, start_date: datetime, end_date: datetime) -> Iterator[List[APIObject]]:
        'Yields pages of API results'

        yield from Underbelly(endpoint, APIObject, start_date, end_date).paginate(20)