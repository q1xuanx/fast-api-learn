from sqlalchemy.orm import Session
from models.models import ItemModel
from dto.request.item_request import ItemsModel
def add_item(db: Session, item : ItemsModel): 
    item_add = ItemModel(
        title = item.title, 
        description = item.description, 
        image_file = item.image
    )
    db.add(item_add)
    db.commit()
    db.refresh(item_add)
    return item_add