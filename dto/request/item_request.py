from pydantic import BaseModel


class ItemsModel(BaseModel): 
    title: str
    description: str
    image: str
    price: float 