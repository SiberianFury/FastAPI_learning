from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/v2/items/{item_id}")
def read_item(item_id: int):
    return {"vvv": item_id}

@app.get('/jopa')
def show_ass():
    # Запрос в базу данных
    return '(_._)'

@app.get('/standname/{standuser_name}')
def name_standuser(standuser_name: str):
    if standuser_name == "Jotaro":
        return {"имя стенда": "Star Platinum"}
    if standuser_name == "Oi_Joskiy":
        return {"имя стенда": "СУМАСШЕДШИЙ КРЭЙЗИ ДАЙМАНКИ"}
    if standuser_name == "DIO":
        return {"имя стенда": "КОНСТРУКТОР ЛЕГО"}
    return {'msg': 'Нет таких юзеров в базе'}