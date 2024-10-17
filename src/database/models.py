from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String
)

from src.database.database import Base

class User(Base):
    __tablename__ = 'User'

    id = Column(
        Integer,
        nullable=False,
        index=True,
        unique=True,
        primary_key=True,
    )

    login = Column(
        String(255),
        nullable=False
    )

    hashed_password = Column(
        String(1024),
        nullable=False
    )

    email = Column(
        String(255),
        uniqe=True,
        index=True
    )

    verify = Column(
        Boolean,
        default=False
    )
