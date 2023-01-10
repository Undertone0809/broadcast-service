# Quick start

## Install
It is recommended to install latest version, which provides more features and less bugs. Old version is shit.

```bash
pip install --upgrade broadcast-service
```

## Initialize
`broadcast-service` use single pattern to build the broadcast pattern/pubsub pattern, which means you can use it like a util class and you didn't initialize any other redundant class.

Now we create a easy pubsub pattern.
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

## Decorator
Moreover, it is recommend to use decorator to listen your topic.

```python
from broadcast_service import broadcast_service


# callback of decorator
@broadcast_service.on_listen(['my_topic'])
def handle_decorator_msg(params):
    print(params)


if __name__ == '__main__':
    info = 'This is very important msg'

    # publish broadcast
    broadcast_service.publish('my_topic', info)
```

You can listen multiple topics by decorator. The function is called back whenever a topic is triggered.

```python
from broadcast_service import broadcast_service


# callback of decorator
@broadcast_service.on_listen(['my_topic'])
def handle_decorator_msg():
    pass


if __name__ == '__main__':
    info = 'This is very important msg'

    # publish broadcast
    broadcast_service.publish('my_topic')
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
