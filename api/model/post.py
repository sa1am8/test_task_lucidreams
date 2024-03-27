import uuid

import sqlalchemy as sa
from database import db
from sqlalchemy import orm


class Post(db.Model):
    __tablename__ = "posts"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    uuid: orm.Mapped[str] = orm.mapped_column(
        sa.String(36),
        unique=True,
        default=uuid.uuid4,
    )

    title: orm.Mapped[str] = orm.mapped_column(sa.String(255))

    author_id: orm.Mapped[int] = orm.mapped_column(
        sa.Integer,
        sa.ForeignKey("users.id"),
    )

    content: orm.Mapped[str] = orm.mapped_column(sa.String(255))

    def __repr__(self):
        return f"<{self.id}: {self.email}>"
