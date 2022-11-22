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

You can also add more params or no params when you publish thr broadcast.
```python
from broadcast_service import broadcast_service

def handle_msg(info, info2):
    print(info)
    print(info2)

if __name__ == '__main__':
    info = 'This is very important msg'
    info2 = 'This is also a very important msg.'

    # listen topic
    broadcast_service.listen('Test', handle_msg)

    # publish broadcast
    broadcast_service.broadcast('Test', info, info2)
```
```python
from broadcast_service import broadcast_service

def handle_msg():
    print('handle_msg callback')

if __name__ == '__main__':
    # listen topic
    broadcast_service.listen('Test', handle_msg)

    # publish broadcast
    broadcast_service.broadcast('Test')
```
Actually, you can see more example in [example](/example).

## TODO
- optimize documents and show more examples.
- optimize the syntax expression of broadcast-service
- provide more test cases


## Contribution
If you want to contribute to this project, you can submit pr or issue. I am glad to see more people involved and optimize it.