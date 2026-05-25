from database.models import UserDB

from utils.password_handler import (
    hash_password,
    verify_password
)


def register_user_service(user, db):

    existing_user = db.query(UserDB).filter(
        UserDB.email == user.email
    ).first()
    

    if existing_user:

        return None

    hashed_password = hash_password(
        user.password
    )

    db_user = UserDB(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


def login_user_service(user, db):

    db_user = db.query(UserDB).filter(
        UserDB.email == user.email
    ).first()

    if not db_user:

        return None

    is_valid = verify_password(
        user.password,
        db_user.password
    )

    if not is_valid:

        return None

    return db_user