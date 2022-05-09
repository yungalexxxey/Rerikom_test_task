from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from schemas import InputSchema, OutputSchema, InputConfirm
from db.db_actions import save_msg, review_msg
from db.alchemy import get_db

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse({"ERROR": "Boolean expected. Got something else instead"}, status_code=400)


@app.post("/api/v1/message", response_model=OutputSchema)
async def add_msg(data: InputSchema, db: Session = Depends(get_db)):
    return save_msg(data.user_id, data.message, db)


@app.post("/api/v1/message_confirmation")
async def conf_msg(request: Request, body: InputConfirm, db: Session = Depends(get_db)):
    return review_msg(request, body.message_id, body.status, db)
