from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from config.database import Base


class Subscription(Base):
    __tablename__ = "Subscriptions"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

