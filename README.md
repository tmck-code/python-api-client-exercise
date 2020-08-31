# Python API Client Exercise

This is a basic fake API Client for developers to interact with, somewhat simulating real-life behaviours.

- [Python API Client Exercise](#python-api-client-exercise)
  - [API Client](#api-client)
  - [Getting Started](#getting-started)
  - [Exercise](#exercise)

## API Client

This repository aims to mimick the experience of using an existing `pip`-packaged client to access data via an API.
This repository contains the code for both the "public-facing" client library, and also the "private/internal" API implementation.

_Only the methods in the "public-facing" client code need to be examined for this exercise. You may examine the API implementation if you wish, but it has been written in a style that is intended to slow down comprehension and reading, and is not required to complete the exercise._

The API client is comprised of **two modules/files**:

- `python_api_client_exercise/api.py` - "public-facing" client library
- `python_api_client_exercise/underbelly.py` - "private/internal" API implementation

There are **three endpoints** that return different items, in different amounts:

- `lists`
- `customers`
- `endpoints`

There is a single method `fetch` that yields pages of api results. **This is the only method that you have to interact with.**

> You may call other methods in this repo directly if you choose, but the aim of this exercise is to implement best-practice usage of the `fetch` method.

```python
class Client:
    def fetch(self, endpoint: str, start_date: datetime, end_date: datetime) -> Iterator[List[APIObject]]:

# The available endpoints can found via the api.ENDPOINTS variable
```

This method yields a paginated response of `APIObject` objects, which contain 3 fields:

<https://github.com/tmck-code/python-api-client-exercise/blob/fc2c5c0fd07678697e51b18ec9a8db3b43a850ef/python_api_client_exercise/api.py#L7-L11>

---

## Getting Started

To kick-start a possible solution, here is an example of how to set up this code for use.

1. Clone this repository
2. Open the python environment of your choice (docker/ipython/python/anaconda/mu/jupyter notebook etc.)
     1. Ensure that the repository is installed via pip:

        ```shell
        pip install git+http://github.com/tmck-code/python-api-client-exercise
        ```

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

## Exercise

1. Make a request to the API `fetch` method.
   > Your solution should involve a method of its own which calls the `fetch` method and deals with the result.
2. Print a lightly-formatted representation of the response data
   > For this step, see the raw output produced by the example code above, and then alter it to log something nicer for each object, and also log any summaries that you might care about after all items have been returned from your request.
3. Handle possible errors
    > The fake API could randomly throw an exception, but otherwise it returns some random fake data based on the "endpoint" that is requested. Your solution should implement some sort of error handling that roughly deals with each kind of error in an appropriate fashion. You should test your implementation before considering this step as done (via running - no unit tests required).
4. (_extension_) Write output to file.
    > After the error handling is fully implemented and tested, alter your solution so that the output from each endpoint is written to its own file on disk. You may choose any output format that you deem appropriate.
