from pydantic import BaseModel
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float


item_dict = {
    'id': 2,
    'name': 'iPhone',
    'description': 'Mobile Gadget',
    'price': 15000
}

# Create an instance from dictionary.
# new_item = Item(**item_dict)
item = Item(id=1, name='Macbook', description='Laptop', price=115000)

print('*'*50)
print(item.id)
print(item.name)
print(item.description)
print('*'*50)

def test(a:str, b:int):
    return a+str(b)

# test('Abhi', 'shek') # Gives warning.
test('Abhi ', 26)


