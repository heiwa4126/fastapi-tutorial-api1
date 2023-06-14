from enum import Enum
from typing import List, Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# https://fastapi.tiangolo.com/ja/tutorial/response-model/
class Message(BaseModel):
    message: str


class User(BaseModel):
    user_id: str


class Model(BaseModel):
    model_name: str
    message: str


class Item(BaseModel):
    item_name: str | None
    item_id: str | None
    owner_id: str | None
    q: str | None
    description: str | None


app = FastAPI()


# https://fastapi.tiangolo.com/ja/tutorial/first-steps/
@app.get("/")
async def root() -> Message:
    return {"message": "Hello World"}


# https://fastapi.tiangolo.com/ja/tutorial/query-params/
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10) -> List[Item]:
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None) -> Item:
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# https://fastapi.tiangolo.com/ja/tutorial/path-params/
@app.get("/users/me")
async def read_user_me() -> User:
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str) -> User:
    return {"user_id": user_id}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
) -> Item:
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) -> Model:
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
