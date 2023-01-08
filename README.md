<h1 align="center">
    broadcast-service
</h1>
<p align="center">
  <strong>A lightweight python broadcast library. You can easily construct a Broadcast pattern/Publish subscriber pattern through this library.</strong>
</p>

<p align="center">
    <a target="_blank" href="">
        <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg?label=license" />
    </a>
   <a target="_blank" href=''>
        <img src="https://img.shields.io/github/stars/Undertone0809/broadcast-service.svg" alt="github stars"/>
   </a>
    <a target="_blank" href=''>
        <img src="https://static.pepy.tech/personalized-badge/broadcast-service?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads/Total"/>
   </a>
    <a target="_blank" href=''>
        <img src="https://static.pepy.tech/personalized-badge/broadcast-service?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads/Week"/>
   </a>
</p>


## Features
- A publishing subscriber pattern can be built with a very simple syntax
- Support different application scenarios, such as asynchronous and synchronous
- Provide different syntax writing modes for lambda, callback functions, decorators, etc

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
