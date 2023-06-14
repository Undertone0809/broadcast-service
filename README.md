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
- A callback function listens on multiple subscriptions
- Provide publisher dispatch callback manage

## Quick Start
- [document github-pages](https://undertone0809.github.io/broadcast-service/#/)
- [document gitee-pages](https://zeeland.gitee.io/broadcast-service/#/)
- [https://pypi.org/project/broadcast-service/](https://pypi.org/project/broadcast-service/)

## Setup

```sh
pip install broadcast-service
```

## Usage
There is an easy demo to show how to use broadcast-service.

```python
from broadcast_service import broadcast_service

# callback of decorator
@broadcast_service.on_listen('my_topic')
def handle_decorator_msg(params):
    print(f"handle_decorator_msg receive params: {params}")

if __name__ == '__main__':
    info = 'This is very important msg'

    # publish broadcast
    broadcast_service.publish('my_topic', info)
```

- You can use `publish, emit, broadcast` to send your topic msg and use `listen, on, subscribe` to listen your topic msg.

- You can also add more arguments or no argument when you publish thr broadcast.

```python
from broadcast_service import broadcast_service

# subscribe topic
@broadcast_service.on_listen(['my_topic'])
def handle_msg(info, info2):
    print(info)
    print(info2)

if __name__ == '__main__':
    info = 'This is very important msg'
    info2 = 'This is also a very important msg.'

    # publish broadcast
    broadcast_service.publish('my_topic', info, info2)
```
```python
from broadcast_service import broadcast_service

# subscribe topic
@broadcast_service.on_listen(['my_topic'])
def handle_msg():
    print('handle_msg callback')

if __name__ == '__main__':
    # publish broadcast
    broadcast_service.publish('Test')
```

You can use `config` to make publisher callback If you want.

```python
from broadcast_service import broadcast_service


@broadcast_service.on_listen("topic")
def handle_subscriber_callback():
    print("handle_subscriber_callback")


def handle_publisher_callback(*args):
    print("handle_publisher_callback")


if __name__ == '__main__':
    broadcast_service.config(
        num_of_executions=5,
        callback=handle_publisher_callback,
        enable_final_return=True,
        interval=0.1
    ).publish("topic")

```

Moreover, you can see more example in [document](https://undertone0809.github.io/broadcast-service/#/).

## TODO
- optimize documents and show more examples.
- ~~optimize the syntax expression of broadcast-service~~
- provide more test cases
- provide the ability to subscribe the topic and callback once
- support for fuzzy subscriptions
- ~~the publisher of the topic can provide a return value~~
- optimize usage in class ('self' params problem)
- build observer mode
- ~~provide publisher callback when all subscriber have completed callback~~


## Contribution
If you want to contribute to this project, you can submit pr or issue. I am glad to see more people involved and optimize it.
