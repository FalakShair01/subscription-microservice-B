from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import models
from config.database import Base, SQLALCHEMY_DATABASE_URL

# Create an in-memory SQLite database for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Dependency to override the database dependency for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

client = TestClient(app)

def test_create_subscription():
    response = client.post("/subscriptions", json={"email": "test@example.com", "is_active": True})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["is_active"] == True

def test_get_all_subscriptions():
    # Create test subscriptions
    db = TestingSessionLocal()
    db.add(models.Subscription(email="test1@example.com", is_active=True))
    db.add(models.Subscription(email="test2@example.com", is_active=False))
    db.commit()

    response = client.get("/subscriptions")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["email"] == "test1@example.com"
    assert data[0]["is_active"] == True
    assert data[1]["email"] == "test2@example.com"
    assert data[1]["is_active"] == False

def test_update_subscription():
    # Create a test subscription
    db = TestingSessionLocal()
    subscription = models.Subscription(email="test@example.com", is_active=True)
    db.add(subscription)
    db.commit()

    # Update the subscription
    updated_data = {"email": "updated@example.com", "is_active": False}
    response = client.put(f"/subscriptions/{subscription.id}", json=updated_data)
    assert response.status_code == 200

    # Retrieve the updated subscription from the database
    updated_subscription = db.query(models.Subscription).filter_by(id=subscription.id).first()
    assert updated_subscription.email == "updated@example.com"
    assert updated_subscription.is_active == False

def test_delete_subscription():
    # Create a test subscription
    db = TestingSessionLocal()
    subscription = models.Subscription(email="test@example.com", is_active=True)
    db.add(subscription)
    db.commit()

    # Delete the subscription
    response = client.delete(f"/subscriptions/{subscription.id}")
    assert response.status_code == 200

    # Verify that the subscription has been deleted from the database
    deleted_subscription = db.query(models.Subscription).filter_by(id=subscription.id).first()
    assert deleted_subscription is None