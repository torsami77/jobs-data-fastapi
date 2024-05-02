from fastapi import APIRouter, HTTPException, Body, Query, status, Depends, Header
import logging
import bleach
from typing import List
from typing_extensions import Annotated, Union

from ..utilities.token import get_current_user, oauth2_scheme


from ..database import models, schemas, db_config


db_gen = db_config.get_db()
db = next(db_gen)

router = APIRouter(
    prefix="/task",
)

severity_list = ['low', 'medium', 'high']
status_list = ['in_progress', 'in_review', 'done']
category_list = ['bug', 'feature', 'chore']

@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=schemas.TaskCreate)
async def create_task(
    title: Annotated[str, Body(min_length=5)],
    category: Annotated[str, Body()],
    severity: Annotated[str, Body()],
    description: Annotated[str, Body()],
    product_id: Annotated[int, Body()],
    token: Annotated[str, Depends(oauth2_scheme)],
):
    current_user = get_current_user(token)
    title = bleach.clean(title)
    category = bleach.clean(category)
    severity = bleach.clean(severity)
    description = bleach.linkify(bleach.clean(description))

    if category not in category_list:
        raise HTTPException(status_code=400, detail=f"'category' must be in {category_list}")
    if severity not in severity_list:
        raise HTTPException(status_code=400, detail=f"'severity' must be in {severity_list}")
    product_exist = db.query(models.User).filter(models.Product.id == product_id).first()
    if not product_exist:
        raise HTTPException(status_code=400, detail=f"No product found with provided id:{product_id}")
    try:
        register_task = models.Task(
            title = title,
            category = category,
            description = description,
            severity = severity,
            status = status_list[0],
            contributors = " ".join([str(current_user["id"])]),
            owner_id = current_user["id"],
            product_id = product_id
        )
        print(register_task, "register_task")
        db.add(register_task)
        db.commit()
        db.refresh(register_task)
        return register_task
    except Exception as error:
        logging.warning(f"Exception Name: {type(error).__name__}")
        logging.warning(f"Exception Desc: {error}")


@router.get('/get_all', status_code=status.HTTP_200_OK, response_model=List[schemas.TaskCreate])
async def get_all_tasks(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        #this query can be paginated to improve performance
        result = db.query(models.Task).all()
        return result
    except Exception as error:
        logging.warning(f"Exception Name: {type(error).__name__}")
        logging.warning(f"Exception Desc: {error}")


@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas.TaskBase)
async def update_task(
    id: int,
    token: Annotated[str, Depends(oauth2_scheme)],
    title: Annotated[Union[str, None], Body(min_length=5)] = None,
    category: Annotated[Union[str, None], Body()] = None,
    severity: Annotated[Union[str, None], Body()] = None,
    task_status: Annotated[Union[str, None], Body()] = None,
    description: Annotated[Union[str, None], Body()] = None,
    product_id: Annotated[Union[int, None], Body()] = None,
):
    current_user = get_current_user(token)
        
    if current_user["role"] != "Employee":
        raise HTTPException(status_code=503, detail="User 'role' must be Employee")
    
    if title:
        title = bleach.clean(title)
    
    if category and category not in category_list:
        raise HTTPException(status_code=400, detail=f"'category' must be in {category_list}")

    if severity and severity not in severity_list:
        raise HTTPException(status_code=400, detail=f"'severity' must be in {severity_list}")

    if task_status and task_status not in status_list:
        raise HTTPException(status_code=400, detail=f"'status' must be in {status_list}")

    if description:
        description = bleach.linkify(bleach.clean(description))

    product_exist = db.query(models.User).filter(models.Product.id == product_id).first()
    if not product_exist:
        raise HTTPException(status_code=400, detail=f"No product found with provided id:{product_id}")

    the_task = db.query(models.Task).filter(models.Task.id == id)
    if the_task.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No task found with provided id:{id}")
    try:
        if title:
            db.query(models.Task).filter(models.Task.id == id).update({'title' : title})
        if category:
            db.query(models.Task).filter(models.Task.id == id).update({'category' : category})
        if severity:
            db.query(models.Task).filter(models.Task.id == id).update({'severity' : severity})
        if task_status:
            db.query(models.Task).filter(models.Task.id == id).update({'status' : task_status})
        if description:
            db.query(models.Task).filter(models.Task.id == id).update({'description' : description})
        if product_id:
            db.query(models.Task).filter(models.Task.id == id).update({'product_id' : product_id})

        db.query(models.Task).filter(models.Task.id == id).update({'contributors' : " ".join([the_task.first().contributors, str(current_user["id"])])})

        db.commit()
        return the_task.first()
    except Exception as error:
        logging.warning(f"Exception Name: {type(error).__name__}")
        logging.warning(f"Exception Desc: {error}")
