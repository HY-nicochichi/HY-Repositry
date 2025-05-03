from pydantic import (
    BaseModel,
    Field
)

class JWTPost(BaseModel):
    mail: str = Field(min_length=1)
    password: str = Field(min_length=1)
