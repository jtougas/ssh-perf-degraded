# ssh-perf-degraded

With `cryptography = "41.0.0"` += 500ms 
```
sed -i 's/^cryptography.*$/cryptography = "41.0.0"/' ./pyproject.toml && \
poetry lock && poetry install && \
poetry run python main.py

...
[2023-06-13 01:02:31,275] [conn=0] Beginning key exchange
[2023-06-13 01:02:31,771] [conn=0] Completed key exchange
...
```

With `cryptography = "40.0.2"` < 100ms
```
sed -i 's/^cryptography.*$/cryptography = "40.0.2"/' ./pyproject.toml && \
poetry lock && poetry install && \
poetry run python main.py

...
[2023-06-13 01:07:40,015] [conn=0] Beginning key exchange
[2023-06-13 01:07:40,091] [conn=0] Completed key exchange
...
```
