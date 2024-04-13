---
# Service B - Subscription Status Synchronization

This service is responsible for synchronizing subscription status updates received from Service A with its own database. It acts as a counterpart to Service A, ensuring consistency in subscription status across different services.

## Description

Service B plays a crucial role in the system's architecture by maintaining subscription status data and updating it based on notifications received from Service A. It provides endpoints for handling subscription status updates and communicates with Service A using RabbitMQ for real-time synchronization.

## Directory Structure


## Directory Structure

```
subscription_microservice/
│
├── config/
│   ├── database.py        # Configuration for database connection
│   └── __init__.py
│
├── model/
│   ├── __init__.py
│   └── models.py           # SQLAlchemy models for database tables
│
├── routers/
│   ├── __init__.py
│   └── subscription.py    # FastAPI routers for handling subscription endpoints
│
├── schemas/
│   ├── __init__.py
│   └── schema.py          # Pydantic schemas for request and response data
│
├── dependencies/
│   ├── __init__.py
│   └── subscription_service.py  # Business logic for subscription management
│
├── main.py                 # FastAPI application setup
├── README.md              # Documentation file
└── requirements.txt       # Project dependencies
```

## Workflow

1. **Request Handling**: FastAPI routers in the `routers` directory handle incoming HTTP requests.
2. **Business Logic**: The business logic for subscription management is implemented in the `subscription_service.py` module inside the `dependencies` directory.
3. **Database Interaction**: Database operations are managed by functions in the `database.py` module inside the `config` directory. SQLAlchemy models for database tables are defined in the `model.py` module inside the `models` directory.
4. **Request/Response Data**: Pydantic schemas for request and response data are defined in the `schema.py` module inside the `schemas` directory.

## Setup

1. **Clone the Repository**: `git clone https://github.com/your-username/subscription_microservice.git`
2. **Navigate to the Project Directory**: `cd subscription-microservice-B`
3. **Create a Virtual Environment**: `python3 -m venv venv`
4. **Activate the Virtual Environment**:
    - On Windows: `venv\Scripts\activate`
    - On macOS and Linux: `source venv/bin/activate`
5. **Install Requirements**: `pip install -r requirements.txt`

## Usage

1. **Run the FastAPI Server**: `uvicorn app:app --reload`
2. **Access the API**: The API is now running locally at `http://localhost:8000`.

## Dependencies

- Python 3.7+
- FastAPI
- SQLAlchemy
- Pydantic
- uvicorn
- rabbitMQ

## Notes

- Ensure that Service A is running and accessible to synchronize subscription status updates using RabbitMQ.
- Update the database configuration in `config/database.py` as needed.
---