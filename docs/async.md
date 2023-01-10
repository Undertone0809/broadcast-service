# Asnychoronous

`broadcast-service` is default asynchronous. Multiple asynchronous tasks can be performed simultaneously. But if you don't want to asynchronous. You can turn off and do as follows:

```python
broadcast_service.enable_async = False
```