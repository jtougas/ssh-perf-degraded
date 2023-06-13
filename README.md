# ssh-perf-degraded

With `cryptography = "41.0.0"`
```
sed -i 's/^cryptography.*$/cryptography = "41.0.0"/' ./pyproject.toml && \
poetry lock && poetry install && \
poetry run python main.py

[2023-06-13 16:00:01,686] Using cryptography 41.0.0
[2023-06-13 16:00:01,686] 1
[2023-06-13 16:00:01,686] 2
[2023-06-13 16:00:01,953] 3
[2023-06-13 16:00:01,953] 4
[2023-06-13 16:00:01,953] 5
[2023-06-13 16:00:02,189] 6
[2023-06-13 16:00:02,192] 7
[2023-06-13 16:00:02,192] 8
```

With `cryptography = "40.0.2"`
```
sed -i 's/^cryptography.*$/cryptography = "40.0.2"/' ./pyproject.toml && \
poetry lock && poetry install && \
poetry run python main.py

[2023-06-13 16:01:04,256] Using cryptography 40.0.2
[2023-06-13 16:01:04,256] 1
[2023-06-13 16:01:04,256] 2
[2023-06-13 16:01:04,324] 3
[2023-06-13 16:01:04,324] 4
[2023-06-13 16:01:04,324] 5
[2023-06-13 16:01:04,324] 6
[2023-06-13 16:01:04,328] 7
[2023-06-13 16:01:04,328] 8
```
