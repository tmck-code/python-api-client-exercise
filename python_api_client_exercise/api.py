from dataclasses import dataclass
from datetime import datetime
from random import randint
from typing import List, Iterator

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
            if ((i+1)%100) == 0 and not bool(randint(0, 2)):
                raise InternalServerError('Server suffered an internal error: DB QUERY TIMEOUT')
            elif ((i+1)%40) == 0 and not bool(randint(0, 4)):
                raise GatewayTimeout('504 Gateway Timeout')
            else:
                yield page