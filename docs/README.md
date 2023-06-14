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

## Setup
```sh
pip install broadcast-service
```


## Usage
There is a easy demo to show how to use broadcast-service.
```python
from broadcast_service import broadcast_service


# callback of common method
def handle_msg(params):
    print(f"handle_msg receive params: {params}")


# callback of decorator
@broadcast_service.on_listen(['my_topic'])
def handle_decorator_msg(params):
    print(f"handle_decorator_msg receive params: {params}")

if __name__ == '__main__':
    info = 'This is very important msg'

    # subscribe topic
    broadcast_service.subscribe('my_topic', handle_msg)

    # publish broadcast
    broadcast_service.publish('my_topic', info)
```

**About more example, please see [Quick Start](/quickstart.md)**

## TODO
- optimize documents and show more examples.
- ~~optimize the syntax expression of broadcast-service~~
- provide more test cases (developing)
- provide the ability to subscribe the topic and callback once
- support for fuzzy subscriptions
- ~~the publisher of the topic can provide a return value~~
- optimize usage in class ('self' params problem)
- build observer mode
- ~~provide publisher callback when all subscriber have completed callback~~


## Contribution
If you want to contribute to this project, you can submit pr or issue. I am glad to see more people involved and optimize it.
