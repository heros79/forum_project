from __future__ import annotations

from typing import List

from pydantic import BaseModel
from pydantic.dataclasses import dataclass

from forum.core.dto.user_info import UserShortInfoResponse


@dataclass
class CommentRequest(BaseModel):
    user_id: int
    content: str


@dataclass
class CommentUpdateRequest(CommentRequest):
    id: int


class CommentResponse(BaseModel):
    id: int
    content: str
    like_count: int
    parent_comment: CommentResponse | None
    child_comments: List[CommentResponse]
    user: UserShortInfoResponse
