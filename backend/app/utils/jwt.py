import jwt
import datetime
import os


def create_access_token(user):
    payload = {
        "user_id": user["id"],
        "username" : user["username"],
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=int(os.getenv("JWT_ACCESS_EXPIRES")))
    }

    return jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")


def create_refresh_token(user):
    payload = {
        "user_id": user["id"],
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=int(os.getenv("JWT_REFRESH_EXPIRES")))
    }

    return jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")


def decode_token(token):
    try:
        print(token)
        return jwt.decode(token, os.getenv("SECRET_KEY"), algorithm="HS256")
    except jwt.ExpiredSignatureError:
        print("error expired")
        print(token)
        return None
    except jwt.InvalidTokenError:
        print("error invalid")
        print(token)
        return None