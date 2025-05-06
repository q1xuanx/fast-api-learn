from fastapi import APIRouter, Depends
from dto.request import item_request as item
from services import item_service
from sqlalchemy.orm import Session
from models.database import get_db
router = APIRouter(prefix='/shop', tags=["Shop"])

@router.get('/')
def get_items(id : int, db: Session = Depends(get_db)):     
    item = item_service.get_item(db, id)
    if item != 'Nothing :D': 
        return {
            "code": 200, 
            "message": 'Find success', 
            "data": item
        }
    return {
            "code": 404, 
            "message": 'Find fail', 
            "data": "Nothing :D"
        }
        

@router.post('/add-item/')
def add_item(item : item.ItemsModel, db: Session = Depends(get_db)): 
    item_service.add_item(db, item)
    return {
        "code": 200, 
        "message": "Add success"
    }
@router.patch('/update-item/')
def update_item(item : item.UpdatedItem, db:Session = Depends(get_db)):
    updated = item_service.update_item(db, item)
    if updated: 
        return {
            "code": 200,
            "message": "Update Complete"
        }
    return {            
        "code": 404,    
        "message": "Error"
    }

@router.delete('/delete/{id}')
def delete_item(id : int, db : Session = Depends(get_db)): 
    deleted = item_service.delete_item(db, id)
    if deleted: 
        return {
            "code": 200,
            "message": "Delete Complete"
        }
    return {
            "code": 404,
            "message": "Item not found"
        }

@router.get('/list')
def get_list(limit : int = 5, current_page : int = 1, db : Session = Depends(get_db)):
    list_item = item_service.get_list(db, limit, (current_page - 1) * limit)
    return {
        "code": 200, 
        "message": "success",
        "data": list_item
    }