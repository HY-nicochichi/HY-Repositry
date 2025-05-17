from typing import Literal
from pydantic import (
    BaseModel,
    Field
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from extensions import TableBase

class User(TableBase):
    mail: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)

class UserPost(BaseModel):
    mail: str = Field(min_length=1)
    password: str = Field(min_length=1)
    name: str = Field(min_length=1)

class UserPut(BaseModel):
    param: Literal['メールアドレス', 'パスワード', 'ユーザーネーム']
    current_val: str = Field(min_length=1)
    new_val: str = Field(min_length=1)
    check_val: str = Field(min_length=1)
