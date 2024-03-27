import uuid

import sqlalchemy as sa
from database import db
from sqlalchemy import orm

from hash_utils import make_hash, hash_verify


class User(db.Model):
    __tablename__ = "users"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    uuid: orm.Mapped[str] = orm.mapped_column(
        sa.String(36),
        unique=True,
        default=uuid.uuid4,
    )
    email: orm.Mapped[str] = orm.mapped_column(
        sa.String(128),
        nullable=True,
        index=True,
        unique=True,
    )

    password_hash: orm.Mapped[str] = orm.mapped_column(sa.String(128), nullable=True)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value: str):
        self.password_hash = make_hash(value)

    def __repr__(self):
        return f"<{self.id}: {self.email}>"

    def check_password(self, password: str) -> bool:
        return hash_verify(password, self.password_hash)
