from pydantic import BaseModel
from pydantic.dataclasses import dataclass

from forum.core.dto.user_info import UserShortInfoResponse


@dataclass
class PostRequest(BaseModel):
    user_id: int
    title: str
    content: str


@dataclass
class PostUpdateRequest(PostRequest):
    id: int


@dataclass
class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    like_count: int
    comment_count: int
    user: UserShortInfoResponse
