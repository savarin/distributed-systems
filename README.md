# distributed-systems

a simple distributed key-value store.

## Quickstart

For the key-value store by itself, run the following command.

```shell
> python src/run.py

0 >
```

This performs as expected.

```shell
0 > set foo bar
set foo: bar

0 > get foo
get foo: bar
``` 

For the client-server, run the following commands in separate terminal windows. For the server:

```shell
> python src/server.py

0 >
```

For client 1:

```shell
> python src/client.py 1

1 >
```

For client 2:

```shell
> python src/client.py 2

2 >
```

Now set and get prompts from the client will be sent to the server.

## Sketch

Class 1

- local key-value store with basic get/set functionality and cli
- support setting value for key, write to disk, and retrieval by key
- stretch goal: support multiple local clients
- use Bencode to serialize/deserialize and format for writes
- use UDP for communication, enqueue/dequeue for serial execution
- use message passing pattern
