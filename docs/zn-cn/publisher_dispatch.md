# Publisher Dispatch

## Publisher Callback
作为一个主题发布者，如何知道所有订阅者的回调函数是否结束了？`broadcast-service`提供了相关的回调机制，在所有的订阅者回调函数结束之后，你可以进行可以回调，
下面这个示例在`handle_subscriber_callback1`和`handle_subscriber_callback2`回调结束时候会进行`handle_publisher_callback`的回调。

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

## Publisher Multiple Executions

`broadcast-service`也支持在同一时间发布多次主题，下面的示例展示了如何在同一时间内进行多次主题的发布。

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

此外，如果你想要设置间隔n秒发送一次主题，你也可以使用interval参数进行时间间隔的配置。

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

结合[publisher-callback](#publisher-callback)部分的内容，你可以让发布者多次发布主题，并且在订阅者回调函数结束之后完成发布者回调函数的回调，
下面这个示例展示了这种功能实现。

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

对于上面的示例，输出结果如下所示。

```text
handle_subscriber_callback
handle_publisher_callback
handle_subscriber_callback
handle_publisher_callback
handle_subscriber_callback
handle_publisher_callback
```

可以看到发布了3次主题，发布者回调函数也执行了三次，如果你想要在所有发布主题、所有订阅者回调函数都执行完之后，最后只执行一次发布者回调函数的话，你
可以使用`enable_final_return=False`的参数设置来达到这种目的。

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

输出结果如下所示，事实上，这种操作方式或许是大多数时候我们想要的结果。

```text
handle_subscriber_callback
handle_subscriber_callback
handle_subscriber_callback
handle_publisher_callback
```


## Return value from subscriber callbacks

发布者的回调当然也可以接收消息，下面一个示例展示了在订阅者的回调函数设置返回值，最终返回给发布者的回调函数。

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

需要注意的是，如果发布者的回调函数必须使用`*args`去接收参数，因为如果有多个订阅者返回信息，发布者的回调就无法设置，因此`*args`作为参数池来接收
从订阅者回调函数中返回回来的参数。`*args`是一个元组，里面可以存储任意类型的数据，只要你可以成功获取到`args`的参数信息。

下面一个示例展示了有多个订阅者回调函数返回信息的复杂场景。

```python
from broadcast_service import broadcast_service


@broadcast_service.on_listen("topic")
def handle_subscriber_callback1():
    return "handle_subscriber_callback 1"


@broadcast_service.on_listen("topic")
def handle_subscriber_callback2():
    return [1,2,3,4,5]

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

需要说明的是，在上面的示例中，`args[0]`, `args[1]`, `args[2]`三个元素的顺序并不是唯一确定的，这需要根据订阅者回调函数的执行时间来判断，但是
在大多数情况下，我们并不能很好的判断哪个订阅者回调函数先结束，因此`broadcast-service`开发规范推荐你在使用这个功能的时候，让订阅者回调函数的返
回值类型尽可能的一致，减少需要额外判断数据的成本。


# Publisher Dispatch

## Publisher Callback
作为一个主题发布者，如何知道所有订阅者的回调函数是否结束了？`broadcast-service`提供了相关的回调机制，在所有的订阅者回调函数结束之后，你可以进行可以回调，
下面这个示例在`handle_subscriber_callback1`和`handle_subscriber_callback2`回调结束时候会进行`handle_publisher_callback`的回调。

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

## Publisher Multiple Executions

`broadcast-service`也支持在同一时间发布多次主题，下面的示例展示了如何在同一时间内进行多次主题的发布。

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

此外，如果你想要设置间隔n秒发送一次主题，你也可以使用interval参数进行时间间隔的配置。

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

结合[publisher-callback](#publisher-callback)部分的内容，你可以让发布者多次发布主题，并且在订阅者回调函数结束之后完成发布者回调函数的回调，
下面这个示例展示了这种功能实现。

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

对于上面的示例，输出结果如下所示。

```text
handle_subscriber_callback
handle_publisher_callback
handle_subscriber_callback
handle_publisher_callback
handle_subscriber_callback
handle_publisher_callback
```

可以看到发布了3次主题，发布者回调函数也执行了三次，如果你想要在所有发布主题、所有订阅者回调函数都执行完之后，最后只执行一次发布者回调函数的话，你
可以使用`enable_final_return=False`的参数设置来达到这种目的。

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

输出结果如下所示，事实上，这种操作方式或许是大多数时候我们想要的结果。

```text
handle_subscriber_callback
handle_subscriber_callback
handle_subscriber_callback
handle_publisher_callback
```


## Return value from subscriber callbacks

发布者的回调当然也可以接收消息，下面一个示例展示了在订阅者的回调函数设置返回值，最终返回给发布者的回调函数。

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

需要注意的是，如果发布者的回调函数必须使用`*args`去接收参数，因为如果有多个订阅者返回信息，发布者的回调就无法设置，因此`*args`作为参数池来接收
从订阅者回调函数中返回回来的参数。`*args`是一个元组，里面可以存储任意类型的数据，只要你可以成功获取到`args`的参数信息。

下面一个示例展示了有多个订阅者回调函数返回信息的复杂场景。

```python
from broadcast_service import broadcast_service


@broadcast_service.on_listen("topic")
def handle_subscriber_callback1():
    return "handle_subscriber_callback 1"


@broadcast_service.on_listen("topic")
def handle_subscriber_callback2():
    return [1,2,3,4,5]

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

需要说明的是，在上面的示例中，`args[0]`, `args[1]`, `args[2]`三个元素的顺序并不是唯一确定的，这需要根据订阅者回调函数的执行时间来判断，但是
在大多数情况下，我们并不能很好的判断哪个订阅者回调函数先结束，因此`broadcast-service`开发规范推荐你在使用这个功能的时候，让订阅者回调函数的返
回值类型尽可能的一致，减少需要额外判断数据的成本。


