# kill server

```shell
lsof -i tcp:3001
kill -9 "32829"

// then double check
lsof -i tcp:3001
```

<img src="./images/kill-server.png" width="1000px"/>
