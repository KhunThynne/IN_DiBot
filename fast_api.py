from typing import Union

from fastapi import FastAPI # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
def generate_html_response():
    with open("static/index.html") as f:
        html_content = f.read()
        return HTMLResponse(content=html_content, status_code=200)


@app.get("/")
async def read_item():
    return generate_html_response()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#uvicorn fast_api:app --reload