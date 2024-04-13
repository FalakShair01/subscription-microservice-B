from sqlalchemy.orm import Session
from model import models
from fastapi import HTTPException

def get_all_subscriptions(db: Session):
    """Retrieve all subscriptions from the database."""
    try:
        return db.query(models.Subscription).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def create_subscription(db: Session, email: str, is_active: bool):
    """Create a new subscription."""
    try:
        subscription = models.Subscription(email=email, is_active=is_active)
        db.add(subscription)
        db.commit()
        db.refresh(subscription)
        return subscription
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_subscription_by_id(db: Session, subscription_id: int):
    """Retrieve a subscription by its ID."""
    try:
        return db.query(models.Subscription).filter(models.Subscription.id == subscription_id).first()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_subscription(db: Session, subscription: models.Subscription, email: str, is_active: bool):
    """Update a subscription."""
    try:
        subscription.email = email
        subscription.is_active = is_active
        db.commit()
        db.refresh(subscription)
        return subscription
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

def delete_subscription(db: Session, subscription: models.Subscription):
    """Delete a subscription."""
    try:
        db.delete(subscription)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


