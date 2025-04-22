from typing import List

from fastapi import FastAPI

from forum.core.dto.comment import CommentRequest, CommentResponse
from forum.core.dto.post import PostRequest, PostResponse, PostUpdateRequest
from forum.core.dto.user_info import UserInfoRequest, UserInfoResponse, UserShortInfoResponse

app = FastAPI()


@app.post(
    "post",
    tags=["Post"],
    summary="Create new Post in Forum",
)
async def create_post(post: PostRequest) -> int:
    return 0


@app.put(
    "/post/{post_id}",
    tags=["Post"],
    summary="Update Post in Forum",
)
async def update_post(post_id: int, post: PostUpdateRequest) -> bool:
    return True


@app.delete(
    "/post/{post_id}",
    tags=["Post"],
    summary="Delete Post in Forum",
)
async def delete_post(post_id: int) -> bool:
    return True


@app.get(
    "/posts",
    tags=["Post"],
    summary="Get all Posts in Forum",
)
async def get_posts(skip: int = 0, limit: int = 15) -> List[PostResponse]:
    return []


@app.get(
    "/post/{post_id}",
    tags=["Post"],
    summary="Get Post in Forum",
)
async def get_post_by_id(post_id: int) -> PostResponse:
    return PostResponse()


@app.get(
    "/author_posts/{author_id}",
    tags=["Post"],
    summary="Get author all posts in Forum",
)
async def get_user_posts(author_id: int, skip: int = 0, limit: int = 15) -> List[PostResponse]:
    return []


@app.get(
    "/post_comments/{post_id}",
    tags=["Comments"],
    summary="Get posts all comments in Forum",
)
async def get_post_comments(post_id: int, skip: int = 0, limit: int = 10) -> List[CommentResponse]:
    return []


@app.post(
    "/comment/{post_id}",
    tags=["Comments"],
    summary="Add comments for post",
)
async def add_comment(post_id: int, comment: CommentRequest) -> int:
    return 0


@app.put(
    "/comment/{comment_id}",
    tags=["Comments"],
    summary="Update comment",
)
async def update_comment(comment_id: int, comment: CommentRequest) -> bool:
    return True


@app.delete(
    "/comment/{comment_id}",
    tags=["Comments"],
    summary="Delete comment",
)
async def delete_comment(comment_id: int) -> bool:
    return True


@app.post(
    "/like_author/{author_id}",
    tags=["Likes"],
    summary="Like author",
)
async def like_author(author_id: int) -> bool:
    return True


@app.post(
    "/unlike_author/{author_id}",
    tags=["Likes"],
    summary="Unlike author",
)
async def unlike_author(author_id: int) -> bool:
    return True


@app.post(
    "/like_post/{post_id}",
    tags=["Likes"],
    summary="Like post",
)
async def like_post(post_id: int) -> bool:
    return True


@app.post(
    "/unlike_post/{post_id}",
    tags=["Likes"],
    summary="Unlike post",
)
async def unlike_post(post_id: int) -> bool:
    return True


@app.post(
    "/like_comment/{comment_id}",
    tags=["Likes"],
    summary="Like comment",
)
async def like_comments(comment_id: int) -> bool:
    return True


@app.post(
    "/unlike_comment/{comment_id}",
    tags=["Likes"],
    summary="Unlike comment",
)
async def unlike_comments(comment_id: int) -> bool:
    return True


@app.post(
    "/follow_author/{author_id}",
    tags=["Follow"],
    summary="Follow user",
)
async def follow_author(author_id: int) -> bool:
    return True


@app.post(
    "/unfollow_author/{author_id}",
    tags=["Follow"],
    summary="Unfollow user",
)
async def unfollow_author(author_id: int) -> bool:
    return True


@app.get(
    "/follow_post/{post_id}",
    tags=["Follow"],
    summary="Follow post",
)
async def follow_post(post_id: int) -> bool:
    return True


@app.post(
    "/unfollow_post/{post_id}",
    tags=["Follow"],
    summary="Unfollow post",
)
async def unfollow_post(post_id: int) -> bool:
    return True


@app.post(
    "/follow_comment/{comment_id}",
    tags=["Follow"],
    summary="Follow comment",
)
async def follow_comment(comment_id: int) -> bool:
    return True


@app.post(
    "/unfollow_comment/{comment_id}",
    tags=["Follow"],
    summary="Unfollow comment",
)
async def unfollow_comment(comment_id: int) -> bool:
    return True


@app.get(
    "/get_user_likes_count/{user_id}",
    tags=["Util"],
    summary="Get user likes count",
)
async def get_user_likes_count(user_id: int) -> int:
    return 0


@app.get(
    "/get_post_likes_count/{post_id}",
    tags=["Util"],
    summary="Get post likes count",
)
async def get_post_likes_count(post_id: int) -> int:
    return 0


@app.get(
    "/get_comment_likes_count/{comment_id}",
    tags=["Util"],
    summary="Get comment likes count",
)
async def get_comment_likes_count(comment_id: int) -> int:
    return 0


@app.post(
    "/user",
    tags=["User Management"],
    summary="Create new user in Forum",
)
async def create_user(user: UserInfoRequest) -> int:
    return 0


@app.put(
    "/user",
    tags=["User Management"],
    summary="Update user info",
)
async def update_user(user: UserInfoRequest) -> UserInfoResponse:
    return UserInfoResponse()


@app.delete(
    "/user/{user_id}",
    tags=["User Management"],
    summary="Delete user in Forum",
)
async def delete_user(user_id: int) -> bool:
    return True


@app.get(
    "/user/{user_id}",
    tags=["User Management"],
    summary="Get user info in Forum",
)
async def get_user(user_id: int) -> UserInfoResponse:
    return UserInfoResponse()


@app.get(
    "/user/{user_id}",
    tags=["User Management"],
    summary="Get user short info in Forum",
)
async def get_user_short(user_id: int) -> UserShortInfoResponse:
    return UserShortInfoResponse()
