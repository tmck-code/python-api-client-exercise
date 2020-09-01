from random import randint
from uuid import uuid1
from datetime import datetime, timedelta
from itertools import zip_longest

class InternalAPIError(Exception):
    'Indicates an unexpected error'

class Underbelly:
    'Here be dragons'

    SCORES = { 'lists': 2, 'customers': 7, 'products': 9 }

    def __init__(self, endpoint, klass, start_date, end_date):
        self.endpoint = endpoint
        self.klass = klass
        self.start_date = start_date
        self.end_date = end_date
        self.n_items = Underbelly.n_items(endpoint, start_date, end_date)

    @staticmethod
    def n_items(endpoint, start_date, end_date):
        return ((end_date - start_date).total_seconds()/86400)*randint(Underbelly.SCORES[endpoint], 10)

    def paginate(self, page_size):
        yield from Underbelly.__paginator_9000(self.gen_items(), page_size)

    def gen_items(self):
        n_days = int((self.end_date - self.start_date).total_seconds()/86400)
        for day in range(0, n_days):
            if day % 100 == 0 and randint(0, 1):
                yield InternalAPIError(f'Database error occurred! Wait 5 seconds and retry your query')
            identifier = str(uuid1())
            for _ in range(int(self.n_items/n_days)):
                yield self.klass(
                    created_at = self.start_date+timedelta(days=day),
                    identifier = identifier,
                    data       = {f'{self.endpoint}_val': randint(0, 10_000)}
                )

    @staticmethod
    def __paginator_9000(items, page_size):
        for group in zip_longest(*[iter(items)]*page_size):
            yield list(filter(None.__ne__, group))