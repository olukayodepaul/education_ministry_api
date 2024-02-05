from app.services.account_opening_service import AccountOpeningService
from app.models.user import User
from app.db.account_opening_schema import AccountOpeningSchema
from sqlalchemy.orm import Session
from unittest.mock import Mock
import pytest

@pytest.fixture
def mock_db_session():
    return Mock(spec=Session)

def test_open_accounts(mock_db_session):
    # Arrange
    account_opening_service = AccountOpeningService(db=mock_db_session)

    # Mock the query method of the database session to return mock data
    mock_db_session.query.return_value.all.return_value = [
        User(id=1, username="user1", email="user1@example.com"),
        User(id=2, username="user2", email="user2@example.com"),
    ]

    # Act
    result = account_opening_service.open_accounts(id=1)

    # Assert
    assert result == [
        User(id=1, username="user1", email="user1@example.com"),
        User(id=2, username="user2", email="user2@example.com"),
    ]

    # Optionally, you can also assert that the query method was called with the expected parameters
    mock_db_session.query.assert_called_once_with(AccountOpeningSchema)
    mock_db_session.query.return_value.all.assert_called_once()
    