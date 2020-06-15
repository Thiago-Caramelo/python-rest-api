import app.routers.users as users
from mock import patch
from uuid import uuid4
import pytest
from fastapi import HTTPException
from app.schemas.user import UserSchema

users_result = [{"name": "name goes here"}]
user_result = {"user": "name"}


def get_users_mock(db, skip, limit):
    return users_result


def test_read_users():
    with patch('app.routers.users.user', autospec=True) as mock_module:
        mock_module.get_users.return_value = users_result
        result = users.read_users(skip=0, limit=0, db=None)
        assert result == users_result
    mock_module.get_users.assert_called_once_with(None, skip=0, limit=0)


def test_read_user():
    uuid4_id = uuid4()
    with patch.object(users.user, 'get_user', return_value=user_result) as mock_method:
        result = users.read_user(uuid4_id, db=None)
        assert result == user_result
    mock_method.assert_called_once_with(None, user_id=uuid4_id)


def test_read_user_not_found():
    uuid4_id = uuid4()
    with patch('app.routers.users.user', autospec=True) as mock_module:
        mock_module.get_user.return_value = None
        with pytest.raises(HTTPException):
            result = users.read_user(uuid4_id, db=None)
    mock_module.get_user.assert_called_once_with(None, user_id=uuid4_id)


def test_create_user():
    with patch('app.routers.users.user', autospec=True) as mock_module:
        new_user = UserSchema(
            id=uuid4(), email="test@test.com", is_active=True)
        mock_module.get_user_by_email.return_value = None
        mock_module.create_user.return_value = new_user
        result = users.create_user(newUser=new_user, db=None)
        assert result == new_user
