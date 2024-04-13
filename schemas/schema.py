from pydantic import BaseModel

class SubscriptionBase(BaseModel):    
    email: str
    is_active: bool



class Subscription(SubscriptionBase):
    id: int

    class Config:
        orm_mode = True

