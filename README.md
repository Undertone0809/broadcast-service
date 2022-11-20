# broadcast-service

broadcast-service is a lightweight python broadcast library. You can easily construct a broadcast pattern through this library.

## Setup

```sh
pip install broadcast-service
```


## Usage

There is a easy demo to show how to use broadcast-service.

```python
from broadcast_service import broadcast_service

def handle_msg(params):
    print(params)

if __name__ == '__main__':
    info = 'This is very important msg'

    # listen topic
    broadcast_service.listen('Test', handle_msg)

    # publish broadcast
    broadcast_service.broadcast('Test', info)

```

## TODO

- optimize documents and show more examples.
- optimize the syntax expression of broadcast-service
- provide more test cases


## Contribution

If you want to contribute to this project, you can submit pr or issue. I am glad to see more people involved and optimize it.