from fastapi import APIRouter, Depends
from dto.request import item_request as item
from services import item_service
from sqlalchemy.orm import Session
from models.database import get_db
router = APIRouter(prefix='/shop', tags=["Shop"])

@router.get('/')
def get_items(): 
    return [{"id": 1, "name": "Shop A"}]


@router.post('/add-item/')
def add_item(item : item.ItemsModel, db: Session = Depends(get_db)): 
    item_service.add_item(db, item)
    return {
        "code": 200, 
        "message": "Add success"
    }