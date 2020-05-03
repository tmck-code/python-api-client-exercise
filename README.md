# Interview Python API

This is a basic fake API for Lexer job applicants to interface with.

- make a request to the API, handle an error and print a formatted response
  - The fake API will randomly throw an exception, but otherwise it returns some
    random fake data that may or may not be formatted correctly
- _extension_: calculate a metric like total spend or somethig

## Real-life inspiration

To design this API similarly to real-life, it is based loosely off the Mailchimp API which we are
familiar with.

There are 3 main endpoints

```
* lists: get/
* lists.members: get/, put/, query/
```

```python
# returns all the lists (only name and id)
client.lists.all(get_all=True, fields="lists.name,lists.id")

# returns all members inside list '123456'
client.lists.members.all('123456', get_all=True)

# return the first 100 member's email addresses for the list with id 123456
client.lists.members.all('123456', count=100, offset=0, fields="members.email_address")

# returns the list matching id '123456'
client.lists.get('123456')

# add John Doe with email john.doe@example.com to list matching id '123456'
client.lists.members.create('123456', {
    'email_address': 'john.doe@example.com',
    'status': 'subscribed',
    'merge_fields': {
        'FNAME': 'John',
        'LNAME': 'Doe',
    },
})

# You are encouraged to specify a value in seconds for the ``timeout``
# parameter to avoid hanging requests.
client = MailChimp('YOUR SECRET KEY', timeout=10.0)

# You are encouraged to specify a User-Agent for requests to the MailChimp
# API. Headers can be specified using the ``request_headers`` parameter.
headers = requests.utils.default_headers()
headers['User-Agent'] = 'Example (example@example.com)'
client = MailChimp('YOUR SECRET KEY', request_headers=headers)
```
