from jose import jwt
from datetime import datetime, timedelta
from config import Config

SECRET_KEY = Config.SECRET_KEY

ALGORITHM = Config.ALGORITHM


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=1)

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt