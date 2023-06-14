# Publisher Dispatch

## Publisher Callback
As a theme publisher, how do you know if all subscriber's callback functions have ended? The `broadcast-service` provides a relevant callback mechanism, and you can make the callback after all subscriber callback functions have ended. The following example conducts `handle_publisher_callback` callback when `handle_subscriber_callback1` and `handle_subscriber_callback2` callbacks end.

```python
from broadcast_service import broadcast_service


@broadcast_service.on_listen("topic")
def handle_subscriber_callback1():
    print("handle_subscriber_callback 1")


@broadcast_service.on_listen("topic")
def handle_subscriber_callback2():
    print("handle_subscriber_callback 2")


def handle_publisher_callback():
    print("handle_publisher_callback")


def main():
    broadcast_service.config(
        callback=handle_publisher_callback,
    ).publish("topic")


if __name__ == '__main__':
    main()

```

**output:**

```text
handle_subscriber_callback 1
handle_subscriber_callback 2
handle_publisher_callback
```

## Publisher Multiple Executions

`broadcast-service` also supports publishing multiple topics at the same time. The following example shows how to publish multiple topics at the same time.

```python
from broadcast_service import broadcast_service

@broadcast_service.on_listen("topic")
def handle_subscriber_callback():
    print("handle_subscriber_callback")

def main():
    broadcast_service.config(
        num_of_executions=5,
    ).publish("topic")

if __name__ == '__main__':
    main()
```

**output**

```text
handle_subscriber_callback
handle_subscriber_callback
handle_subscriber_callback
handle_subscriber_callback
handle_subscriber_callback
```

In addition, if you want to set the time interval to send topics every n seconds, you can also use the `interval` parameter to configure the time interval.

```python
from broadcast_service import broadcast_service

@broadcast_service.on_listen("topic")
def handle_subscriber_callback():
    print("handle_subscriber_callback")

def main():
    broadcast_service.config(
        num_of_executions=5,
        interval=2 # 2seconds
    ).publish("topic")

if __name__ == '__main__':
    main()

```

Combining the content of the [publisher-callback](#publisher-callback) section, you can make the publisher publish topics multiple times and complete the publisher callback function after all subscriber callback functions are executed. The following example shows how to implement this function.

```python
from broadcast_service import broadcast_service


@broadcast_service.on_listen("topic")
def handle_subscriber_callback():
    print("handle_subscriber_callback")


def handle_publisher_callback():
    print("handle_publisher_callback")


def main():
    broadcast_service.config(
        num_of_executions=3,
        callback=handle_publisher_callback
    ).publish("topic")


if __name__ == '__main__':
    main()
```

For the above example, the output is as follows:

```text
handle_subscriber_callback
handle_publisher_callback
handle_subscriber_callback
handle_publisher_callback
handle_subscriber_callback
handle_publisher_callback
```

It can be seen that the topic was published three times, and the publisher callback function was executed three times. If you want the publisher callback function to be executed only once after all topics are published and all subscriber callback functions are executed, you can use the parameter `enable_final_return=False` to achieve this goal.

```python
from broadcast_service import broadcast_service


@broadcast_service.on_listen("topic")
def handle_subscriber_callback():
    print("handle_subscriber_callback")


def handle_publisher_callback():
    print("handle_publisher_callback")


def main():
    broadcast_service.config(
        num_of_executions=3,
        callback=handle_publisher_callback,
        enable_final_return=True
    ).publish("topic")


if __name__ == '__main__':
    main()
```

The output is as follows, and in fact, this way of operation may be the result we want most of the time.

```text
handle_subscriber_callback
handle_subscriber_callback
handle_subscriber_callback
handle_publisher_callback
```


## Return value from subscriber callbacks

The publisher's callback function can also receive messages. The following example shows how to set return values in the subscriber's callback function and finally return them to the publisher's callback function.

```python
from broadcast_service import broadcast_service


@broadcast_service.on_listen("topic")
def handle_subscriber_callback():
    return "handle_subscriber_callback"


def handle_publisher_callback(*args):
    print(args[0])  # "handle_subscriber_callback"


def main():
    broadcast_service.config(
        callback=handle_publisher_callback,
    ).publish("topic")


if __name__ == '__main__':
    main()

```

Note that if the publisher's callback function needs to receive parameters, you must use `*args` to receive parameters. Therefore, if multiple subscriber callback functions return information, the publisher's callback cannot be set. Therefore, `*args` is used as a parameter pool to receive data returned from the subscriber's callback function. `*args` is a tuple, which can store any type of data, as long as you can successfully obtain the parameter information of `args`.

The following example shows a complex scenario where multiple subscriber callback functions return information.

```python
from broadcast_service import broadcast_service


@broadcast_service.on_listen("topic")
def handle_subscriber_callback1():
    return "handle_subscriber_callback 1"


@broadcast_service.on_listen("topic")
def handle_subscriber_callback2():
    return [1, 2, 3, 4, 5]


@broadcast_service.on_listen("topic")
def handle_subscriber_callback3():
    return {"key": "value"}


def handle_publisher_callback(*args):
    print(args[0])  # "handle_subscriber_callback 1"
    print(args[1])  # [1,2,3,4,5]
    print(args[2])  # {"key", "value"}


def main():
    broadcast_service.config(
        callback=handle_publisher_callback,
    ).publish("topic")


if __name__ == '__main__':
    main()
```

It should be noted that the order of the three elements `args[0]`, `args[1]`, and `args[2]` in the above example is not uniquely determined, which depends on the execution time of the subscriber's callback function. However, in most cases, we cannot judge which subscriber callback function ends first, so `broadcast-service` development specifications recommend that when using this function, let the return value types of the subscriber callback functions be consistent as much as possible to reduce the cost of additional data judgment.