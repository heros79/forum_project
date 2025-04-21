from typing import List

from fastapi import FastAPI


app = FastAPI()


@app.post("post")
async def create_post(post: PostRequest) -> int:
    pass


@app.put("/post/{post_id}")
async def update_post(post_id: int, post: PostRequest) -> bool:
    pass


@app.delete("/post/{post_id}")
async def delete_post(post_id: int) -> bool:
    pass


@app.get("/posts")
async def get_posts(skip: int = 0, limit: int = 15) -> List[PostResponse]:
    pass


@app.get("/post/{post_id}")
async def get_post_by_id(post_id: int) -> PostResponse:
    pass


@app.get("/author_posts/{author_id}")
async def delete_post_by_id(author_id: int, skip: int = 0, limit: int = 15) -> List[PostResponse]:
    pass


@app.get("/post_comments/{post_id}")
async def get_post_comments(post_id: int, skip: int = 0, limit: int = 10) -> List[CommentResponse]:
    pass


@app.post("/comment/{post_id}")
async def add_comment(post_id: int, comment: CommentRequest) -> int:
    pass


@app.put("/comment/{comment_id}")
async def update_comment(comment_id: int, comment: CommentRequest) -> bool:
    pass


@app.delete("/comment/{comment_id}")
async def delete_comment(comment_id: int) -> bool:
    pass


@app.post("/like_author/{author_id}")
async def like_author(author_id: int) -> bool:
    pass


@app.post("/unlike_author/{author_id}")
async def unlike_author(author_id: int) -> bool:
    pass


@app.post("/like_post/{post_id}")
async def like_post(post_id: int) -> bool:
    pass


@app.post("/unlike_post/{post_id}")
async def unlike_post(post_id: int) -> bool:
    pass


@app.post("/like_comment/{comment_id}")
async def like_comments(comment_id: int) -> bool:
    pass


@app.post("/unlike_comment/{comment_id}")
async def unlike_comments(comment_id: int) -> bool:
    pass


@app.post("/follow_author/{author_id}")
async def follow_author(author_id: int) -> bool:
    pass


@app.post("/unfollow_author/{author_id}")
async def unfollow_author(author_id: int) -> bool:
    pass


@app.get("/follow_post/{post_id}")
async def follow_post(post_id: int) -> bool:
    pass


@app.post("/unfollow_post/{post_id}")
async def unfollow_post(post_id: int) -> bool:
    pass


@app.post("/follow_comment/{comment_id}")
async def follow_comment(comment_id: int) -> bool:
    pass


@app.post("/unfollow_comment/{comment_id}")
async def unfollow_comment(comment_id: int) -> bool:
    pass


@app.get("/get_user_likes_count/{user_id}")
async def get_user_likes_count(user_id: int) -> int:
    pass


@app.get("/get_post_likes_count/{post_id}")
async def get_post_likes_count(post_id: int) -> int:
    pass


@app.get("/get_comment_likes_count/{comment_id}")
async def get_comment_likes_count(comment_id: int) -> int:
    pass


@app.post("/user")
async def create_user(user: UserInfoRequest) -> int:
    pass


@app.put("/user")
async def update_user(user: UserInfoRequest) -> UserInfo:
    pass


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> bool:
    pass


@app.get("/user/{user_id}")
async def get_user(user_id: int) -> UserInfo:
    pass
