"""API script for {{cookiecutter.pkg_name}}."""

import json
import typing
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI()


# pylint: disable=too-few-public-methods
class Item(BaseModel):
    """
    A template put request item

    Args:
        BaseModel (pydantic.BaseModel): pydantic BaseModel base class
    """

    id: int
    name: str


class PrettyJSONResponse(Response):
    """
    Creates a prettified JSON output from a starlette Response

    Args:
        Response (starlette.responses.Response): the response to prettify

    Returns:
        str: prettified JSON string
    """

    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")


@app.get("/")
def read_root() -> str:
    """
    Get the api name and version

    Returns:
        str: the api name and version
    """

    return "{{ cookiecutter.project_slug }} {{ cookiecutter.version }}"


@app.get("/items/{item_id}")
def read_item(item_id: int, query: Optional[str] = None) -> dict:
    """
    Template for a get request

    Args:
        item_id (int): an item id
        query (Union[str, None], optional): a query parameter. Defaults to None.

    Returns:
        dict: item_id and query
    """

    return {"item_id": item_id, "query": query}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> dict:
    """
    Template for a put request

    Args:
        item_id (int): an item id
        item (Item): the put request body

    Returns:
        dict: the name of the item in the payload, and the id
    """

    return {"item_name": item.name, "item_id": item_id}


def run() -> None:
    """launch the api"""

    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
