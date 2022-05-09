from sqlalchemy.orm import Session
from .db_model import DbMsg
from fastapi import Request
from .kafka_prod import producer
import jwt

TOKEN = "AUTH_TOKEN"


def save_msg(user_id: int, msg: str, db: Session):
    new_msg = DbMsg(
        id=user_id,
        message=msg,
        status="review"
    )
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    producer.send("topic_test", value={'message_id': new_msg.message_id, 'message': new_msg.message})
    return new_msg


def review_msg(request: Request, msg_id: int, msg_stat: bool, db: Session):
    input_token = request.headers.get("Authorization")
    adapter = {True: "correct", False: "blocked"}
    decoded_token = ""
    try:
        decoded_token = jwt.decode(input_token, "best_password", algorithms=["HS256"]).get("Token")
    except:
        pass
    if decoded_token != TOKEN:
        return {"ERROR": "Wrong Token"}
    msg: DbMsg = db.query(DbMsg).filter(DbMsg.message_id == msg_id).first()
    if not msg:
        return {"ERROR": f"No message with {msg_id} id"}
    msg.status = adapter[msg_stat]
    db.commit()
    db.refresh(msg)
    return msg
