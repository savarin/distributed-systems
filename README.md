# distributed-systems

- Class 1
  - local key-value store with basic get/set functionality and cli
  - support setting value for key, write to disk, and retrieval by key
  - stretch goal: support multiple local clients

  - use Bencode to serialize/deserialize and format for writes
  - use UDP for communication, enqueue/dequeue for serial execution
  - use message passing pattern
