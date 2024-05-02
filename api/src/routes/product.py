from fastapi import APIRouter, HTTPException, Body, Query, status, Depends
import logging
import bleach
from typing import List
from typing_extensions import Annotated

from ..utilities.token import oauth2_scheme


from ..database import models, schemas, db_config

db_gen = db_config.get_db()
db = next(db_gen)

router = APIRouter(
    prefix="/product",
)

@router.get('/get_all', status_code=status.HTTP_200_OK, response_model=List[schemas.Product])
async def get_all_products(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        #this query can be paginated to improve performance
        result = db.query(models.Product).all()
        return result
    except Exception as error:
        logging.warning(f"Exception Name: {type(error).__name__}")
        logging.warning(f"Exception Desc: {error}")
