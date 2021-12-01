from python_api_client_exercise import api
from datetime import datetime

client = api.Client('access_token', 'access_token_secret')

for endpoint in api.ENDPOINTS:
    print(f"Fetching {endpoint}")

    results = client.fetch(
        endpoint,
        start_date = datetime(2021, 1, 1),
        end_date   = datetime(2021, 2, 1)
    )

    for page in results:
        print(page)
