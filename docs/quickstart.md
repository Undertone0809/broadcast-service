# Quick start

## Install
It is recommended to install latest version, which provides more features and less bugs. The old version is shit.

```bash
pip install --upgrade broadcast-service
```

## Example
`broadcast-service` use single pattern to build the broadcast pattern/pubsub pattern, which means you can use it like a util class and you didn't initialize any other redundant class.

<p align='center'>
    <img src="https://zeeland-bucket.oss-cn-beijing.aliyuncs.com/typora_img/20230111230418.png"/>
</p>

**Now you can see a easy pubsub pattern.**
```python
from broadcast_service import broadcast_service


# callback of common method
def handle_msg(params):
    print(params)


if __name__ == '__main__':
    info = 'This is very important msg'

    # subscribe topic
    broadcast_service.subscribe('my_topic', handle_msg)

    # publish broadcast
    broadcast_service.publish('my_topic', info)

```

> :warning: Attention: `listen` and `subscribe` mean the same thing in the following passage.

## How to subscribe?
Actually, `broadcast-service` support mutiple subscirbe and publish methods, such as `common callback function` and `decorator`. You can see more example as follows.

- **subscribe single topic**

```python
from broadcast_service import broadcast_service


# common callback function method
def handle_msg(params):
    print(params)


# decorator method
@broadcast_service.on_listen(['my_topic'])
def handle_decorator_msg1(params):
    print(params)


# if you just listen one topic, you don't have to pass a topic list
@broadcast_service.on_listen("my_topic")
def handle_decorator_msg2(params):
    print(params)


if __name__ == '__main__':
    info = 'This is very important msg'

    # subscribe topic
    broadcast_service.subscribe('my_topic', handle_msg)
    # you can also pass a topics list to subscribe multiple topics
    broadcast_service.subscribe(['my_topic'], handle_msg)

    # publish broadcast
    broadcast_service.publish('my_topic', info)
```

- **subscribe multiple topics**

<p align='center'>
    <img src="https://zeeland-bucket.oss-cn-beijing.aliyuncs.com/typora_img/20230111230943.png"/>
</p>

```python
from broadcast_service import broadcast_service


def handle_msg(params):
    print(params)


@broadcast_service.on_listen(['my_topic1', 'my_topic2'])
def handle_decorator_msg(params):
    print(params)


if __name__ == '__main__':
    # This callback function is triggered when a message is sent from one of two topics subscribed to
    broadcast_service.subscribe(['my_topic1', 'my_topic2'], handle_msg)

    # publish broadcast
    broadcast_service.publish('my_topic1', "msg1")
    broadcast_service.publish('my_topic2', "msg2")
```

## How to publish?
You can pass multiple arguments to a topic or multiple topics by `broadcast-service`. You can see more example as follows.

- **publish a topic**

```python
from broadcast_service import broadcast_service


@broadcast_service.on_listen("no_param")
def handle_no_param():
    print("no param")

broadcast_service.publish("no_param")


@broadcast_service.on_listen("one_param")
def handle_one_param(params):
    print(params)

broadcast_service.publish("one_param", 123)


@broadcast_service.on_listen("three_params")
def handle_three_params(a, b, c):
    print(a)
    print(b)
    print(c)

broadcast_service.publish("one_param", 11, 22, 33)


@broadcast_service.on_listen("multi_params")
def handle_multi_params(*args, **kwargs):
    print(args) # [11, 22]
    print(kwargs['msg']) # hello

broadcast_service.publish("one_param", 11, 22, msg="hello")
```

## Argument
About argument, you'd better know how many arguments you should take. If your callback function arguments is different from the message arguments of your publish, you may not recevice the callback. Here are some example:

- True :heavy_check_mark:


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
- True :heavy_check_mark:

```python
from broadcast_service import broadcast_service


# subscribe topic
@broadcast_service.on_listen(['my_topic'])
def handle_msg(*args, **kwargs):
    print('handle_msg callback')


if __name__ == '__main__':
    # publish broadcast
    broadcast_service.publish('Test')
```

- False :no_entry_sign:

```python
from broadcast_service import broadcast_service


# subscribe topic
@broadcast_service.on_listen(['my_topic'])
def handle_msg(a, b, c):
    print('handle_msg callback')


if __name__ == '__main__':
    # publish broadcast
    broadcast_service.publish('Test')
```
> It is recommented your argument setting `*args, **kwargs` if you don't know how many arguments you need take. Sometime you can use `kwargs` as a dictionary to pass your arguments.

If you listen mulitple topics of different number of arguments. The best choose is use `*args, **kargs`.

```python
from broadcast_service import broadcast_service


@broadcast_service.on_listen()
def handle_decorator_msg(*args, **kwargs):
    print(kwargs)


if __name__ == '__main__':
    broadcast_service.publish('my_topic1', params=[11,22])
    broadcast_service.publish('my_topic2', params={"msg": "success"})
```

**output:**

```text
{'params': [11, 22]}
{'params': {'msg': 'success'}}
```

## Attention
You can use `publish, emit, broadcast` to send your topic msg. Using `listen, on, subscribe` to listen your topic msg. Using `stop_listen, off, unsubscribe` to cancel subscribe.


```python
# send topic msg
broadcast_service.subscribe('my_topic', handle_msg)
broadcast_service.listen('my_topic', handle_msg)
broadcast_service.on('my_topic', handle_msg)


# listen topic msg
broadcast_service.broadcast('my_topic', info)
broadcast_service.publish('my_topic', info)
broadcast_service.emit('my_topic', info)
```
