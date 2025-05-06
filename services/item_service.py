from sqlalchemy import null
from sqlalchemy.orm import Session
from models.models import ItemModel
from dto.request.item_request import ItemsModel, UpdatedItem

def add_item(db: Session, item : ItemsModel): 
    item_add = ItemModel(
        title = item.title, 
        description = item.description, 
        image_file = item.image,
        price = item.price
    )
    db.add(item_add)
    db.commit()
    db.refresh(item_add)
    return item_add

def get_item(db: Session, id : int): 
    item = db.query(ItemModel).filter(ItemModel.id == id).first()
    db.close()
    if item != None:
        return item 
    return 'Nothing :D'

def update_item(db: Session, item_update: UpdatedItem): 
    item = db.query(ItemModel).filter_by(id=item_update.id).first()
    if item == None: 
        return 'Not found item'
    item.description = item_update.description
    item.image_file = item_update.image
    item.price = item_update.price
    item.title = item_update.title
    db.commit()
    return item

def delete_item(db : Session, id_item : int): 
    item = db.query(ItemModel).filter_by(id=id_item).first()
    if item != None: 
        db.delete(item)
        return True
    return False
    
def get_list(db : Session, limit : int, skip : int): 
    list_item = db.query(ItemModel).group_by(ItemModel.id).limit(limit).offset(skip).all()
    return list_item
    