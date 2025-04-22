from pydantic import BaseModel, EmailStr
from pydantic.dataclasses import dataclass


@dataclass
class UserInfoRequest(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None
    photo_url: str | None
    nickname: str
    email: EmailStr


@dataclass
class UserShortInfoResponse(BaseModel):
    id: int
    photo_url: str | None
    nickname: str


@dataclass
class UserInfoResponse(UserShortInfoResponse):
    name: str
    last_name: str
    middle_name: str | None
    email: EmailStr
    followers_count: int
    following_count: int
