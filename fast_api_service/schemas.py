from pydantic import BaseModel


class InputSchema(BaseModel):
    user_id: int
    message: str


class OutputSchema(BaseModel):
    message_id: int
    status: str

    class Config:
        orm_mode = True


class InputConfirm(BaseModel):
    message_id: int
    status: bool
