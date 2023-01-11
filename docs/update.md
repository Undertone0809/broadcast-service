# Update

## Upgrade Version
Please update the latest version. The old version is shit.

```bash
pip install --upgrade broadcast-service
```

## v1.2.0 2023-01-12

#### feat
1. Add support multiple publications and multiple subscriptions.

```python
broadcast_service.publish(["topic1", "topic2"], "message")
```

2. Optimize the function of `broadcast_service.subscribe()` and `broadcast_service.publish()`

- The following two cases are equivalent.

```python
@broadcast_service.on_listen(['topic1'])
def handle_all_msg():
    # your code

@broadcast_service.on_listen('topic1')
def handle_all_msg():
    # your code

```

```python
broadcast_service.subscribe('topic1')
broadcast_service.subscribe(['topic1'])
```


#### test
1. Add more test cases


## v1.1.7 2023-01-10

#### feat

1. Add decorator, optimize syntactic expression [#5](https://github.com/Undertone0809/broadcast-service/pull/5) 

- You can use the following sentences to subscribe topic

```python
@broadcast_service.on_listen(['topic1'])
def handle_all_msg():
    # your code

@broadcast_service.on_listen(['topic1','topic2'])
def handle_all_msg():
    # your code

@broadcast_service.on_listen()
def handle_all_msg(*args, **kwargs):
    # your code
```

2. Add some equals function name

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

#### test

1. Optimize test cases and add some demo [#5](https://github.com/Undertone0809/broadcast-service/pull/5) 
