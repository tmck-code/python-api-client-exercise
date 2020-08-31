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

class ServerError(Exception):
    'Indicates a 5XX error'

class GatewayTimeout(Exception):
    'Indicates 504 Gateway Timeout'

class InternalServerError(Exception):
    'Indicates 500 Internal Server Error'

class ClientError(Exception):
    'Indicates a 4XX error'

@dataclass
class Client:
    access_token_key:    str
    access_token_secret: str

    PAGE_SIZE = 20

    def fetch(self, endpoint: str, start_date: datetime, end_date: datetime) -> Iterator[List[APIObject]]:
        'Yields pages of API results'

        response = Underbelly(endpoint, APIObject, start_date, end_date).paginate(Client.PAGE_SIZE)
        for i, page in enumerate(response):
            if i % 100 == 0:
                raise InternalServerError('Server suffered an internal error: DB QUERY TIMEOUT')
            if i % 40 == 0:
                raise GatewayTimeout('504 Gateway Timeout')
            yield page
