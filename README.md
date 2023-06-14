# fastapi-tutorial-api1

[最初のステップ - FastAPI](https://fastapi.tiangolo.com/ja/tutorial/first-steps/)
をやってみた。

## 始め方

```bash
# bash
./set_venv_here.sh
. .venv/bin/activate

# powershell
./set_venv_here.ps1
```

## 開発

```bash
# bash
./dev.sh

# powershell
./dev.ps1
```

最初のテストは

```bash
curl http://127.0.0.1:8000
```

ドキュメントは

- [FastAPI - Swagger UI](http://127.0.0.1:8000/docs)
- [FastAPI \- ReDoc](http://127.0.0.1:8000/redoc)

OpenAPIは <http://127.0.0.1:8000/openapi.json> で取れる。
