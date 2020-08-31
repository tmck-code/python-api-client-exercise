# Python API Client Exercise

This is a basic fake API Client for developers to interact with, somewhat simulating real-life behaviours.

- [Python API Client Exercise](#python-api-client-exercise)
  - [Exercise](#exercise)
  - [Real-life inspiration](#real-life-inspiration)
  - [Solution](#solution)

## Exercise

1. make a request to the API
2. handle possible errors
3. print a lightly formatted representation of the response data
    > The fake API will randomly throw an exception, but otherwise it returns some random fake data based on the "endpoint" that is requested.
4. _extension_: write output to file

## Real-life inspiration

There are several main endpoints that return different items, in different amounts
> e.g. len(lists) < len(customers) < len(products)

There is a single method `fetch` that yields pages of api results. **This is the only method that you have to interact with.**

> You may call other methods in this repo directly if you choose, but the aim of this exercise is to implement best-practice usage of the `fetch` method.

```python
 def fetch(self, endpoint: str, start_date: datetime, end_date: datetime) -> Iterator[List[APIObject]]:
```

## Solution

To kick-start a possible solution, here is an example of how to set up this code for use.

1. Clone this repository
2. Open the python environment of your choice (docker/ipython/python/anaconda/mu/jupyter notebook etc.)
   1. Ensure that the requirements (and optionally the repo itself) are pip-installed.
      `pip install repo`

3. Paste the following code:

    ```python
    from python_api_client_exercise import api
    from datetime import datetime

    client = api.Client('access_token', 'access_token_secret')

    for endpoint in api.ENDPOINTS:
        print(endpoint)
        results = client.fetch(endpoint, start_date=datetime(2020, 1, 1), end_date=datetime(2020, 2, 1))
        for data in results:
          print(data)
    ```

4. Now, navigate up to the [Exercise](#exercise) section and implement as many of the requirements (in-order) as you can!