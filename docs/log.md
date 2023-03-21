# Log

If you want to open the log mode, you should do as follows:

```python
from broadcast_service import broadcast_service, enable_log

enable_log()


@broadcast_service.on_listen("test")
def handle_msg():
    print('handle msg')


broadcast_service.publish('test')

```


- result

<img src="https://zeeland-bucket.oss-cn-beijing.aliyuncs.com/images/20230321132348.png"/>