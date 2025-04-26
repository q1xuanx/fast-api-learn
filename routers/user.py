from fastapi import APIRouter

router = APIRouter(prefix='/user', tags=["users"])


@router.get('/{name}')
def say_hello(name : str): 
    return {
        'code': 200, 
        'message': f'Hello {name}'
    }
