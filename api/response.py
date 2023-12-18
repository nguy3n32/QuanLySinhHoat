from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Message(BaseModel):
    detail: str


response = {
    409: {409: {"model": Message, "detail": "The item was duplicate"}},
    404: {404: {"model": Message, "detail": "NotFound"}},
    500: {500: {"model": Message, "detail": "Internal Error"}}
}


def duplicate_response(value: str):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT,
                        content={"detail": f"{value} already exist in the database"})


not_found_response = JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                                  content={"detail": "Can't found any in the system"})


Not_Found_Exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Can't found any in the system"
)


InternalError = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Internal Server Error"
)