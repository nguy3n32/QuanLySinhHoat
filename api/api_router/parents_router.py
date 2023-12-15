from fastapi import APIRouter
from app.models.parents import ParentRead, ParentsCreate
from app.api.depends import SessionDep
from app.crud import parents_crud

parents_router = APIRouter()


@parents_router.get("/", response_model=ParentRead)
async def get_all():
    return ParentRead(
        full_name="Nguyen",
        address="Da Nang",
        email="Nguyen@123.coom"
    )


@parents_router.post("/add-parent", response_model=ParentRead)
async def add_parent(new_parent: ParentsCreate, session: SessionDep):
    return parents_crud.add_parent(new_parent, session)
