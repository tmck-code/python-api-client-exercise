# Interview Python API

This is a basic fake API for Lexer job applicants to interface with.

- make a request to the API, handle an error and print a formatted response
  - The fake API will randomly throw an exception, but otherwise it returns some
    random fake data that may or may not be formatted correctly
- _extension_: calculate a metric like total spend or somethig

## Real-life inspiration

There are several main endpoints that return different items, in different amounts
> e.g. len(lists) < len(customers) < len(products)

There is a single method `fetch` that yields pages of api results.
