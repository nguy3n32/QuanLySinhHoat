from typing import List
from fastapi import APIRouter

from app.models.parents import ParentRead, ParentsCreate
from app.models.linked_schemas import ParentWithChild
from app.api.depends import SessionDep
from app.crud import parents_crud

parents_router = APIRouter()


@parents_router.get("/", response_model=List[ParentWithChild])
async def get_all(session: SessionDep):
    return parents_crud.get_all_parents(db=session)


@parents_router.post("/add-parent", response_model=ParentRead)
async def add_parent(new_parent: ParentsCreate, session: SessionDep):
    return parents_crud.add_parent(new_parent, session)
