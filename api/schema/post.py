from pydantic import BaseModel, ConfigDict


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

    model_config = ConfigDict(
        from_attributes=True,
    )


class PostsOut(BaseModel):
    posts: list[PostOut]


class PostCreate(BaseModel):
    title: str
    content: str
