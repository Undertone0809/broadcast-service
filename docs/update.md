# Update

## Upgrade Version
Please update the latest version. The old version is shit.

```bash
pip install --upgrade broadcast-service
```
## v2.1.0 2023-06-15

#### feat
1. Add split_parameters for config(). [#docs](publisher_dispatch?id=passing-different-parameters-when-publishing-a-topic-multiple-times)

## v2.0.0 2023-06-14

#### feat
1. Add publisher dispatch config. It can publish topic with a complex mode. [#12](https://github.com/Undertone0809/broadcast-service/pull/12)
- provide publisher callback
- provide the return value of subscriber callbacks
- provide multiple call publish at once
- provide multiple call time interval

## v1.3.1 2023-06-02

#### fix
1. Add singleton to keep only one `broadcast_service` instance in an application [#11](https://github.com/Undertone0809/broadcast-service/pull/11)

## v1.3.0 2023-03-21

#### feat
1. Add log mode. [Detail Information](./log.md)

#### fix
1. optimize some code structure

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
