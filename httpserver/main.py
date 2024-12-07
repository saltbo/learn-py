from time import sleep, time
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def read_root():
    print(time())
    return {"Hello": "World"}


@app.get("/abc")
async def abc():
    # 标记了async，但是没有任何异步逻辑，写出了一个异步阻塞函数。这种情况下如果只有一个worker会阻塞其他请求
    n = 0
    while n < 10:
        n += 1
        sleep(1)
    return {"abc": 123}


@app.get("/items/{item_id}", name="hello12", description="abc")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import uvicorn
    print(123, uvicorn.__version__)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=3)
