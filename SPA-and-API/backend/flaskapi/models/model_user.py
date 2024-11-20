from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from extensions import TimeStampModel

class User(TimeStampModel):

    __tablename__ = 'users'

    user_id: Mapped[str] = mapped_column(nullable=False, primary_key=True)
    mail_address: Mapped[str] = mapped_column(nullable=False, unique=True)
    encrypted_pass: Mapped[str] = mapped_column(nullable=False)
    user_name: Mapped[str] = mapped_column(nullable=False)
