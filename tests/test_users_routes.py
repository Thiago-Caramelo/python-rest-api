import app.routers.users as users
import mock
import uuid
import pytest
import fastapi
import app.schemas.user as user_schema
import app.database.models.user as user_database

users_result = [{"name": "name goes here"}]
user_result = {"user": "name"}


def get_users_mock(db, skip, limit):
    return users_result


def test_read_users():
    with mock.patch('app.routers.users.user', autospec=True) as mock_module:
        mock_module.get_users.return_value = users_result
        result = users.read_users(skip=0, limit=0, db=None)
        assert result == users_result
    mock_module.get_users.assert_called_once_with(None, skip=0, limit=0)


def test_read_user():
    uuid4_id = uuid.uuid4()
    with mock.patch.object(users.user, 'get_user', return_value=user_result) as mock_method:
        result = users.read_user(uuid4_id, db=None)
        assert result == user_result
    mock_method.assert_called_once_with(None, user_id=uuid4_id)


def test_read_user_not_found():
    uuid4_id = uuid.uuid4()
    with mock.patch('app.routers.users.user', autospec=True) as mock_module:
        mock_module.get_user.return_value = None
        with pytest.raises(fastapi.HTTPException):
            result = users.read_user(uuid4_id, db=None)
    mock_module.get_user.assert_called_once_with(None, user_id=uuid4_id)


def test_create_user():
    with mock.patch('app.routers.users.user', autospec=True) as mock_module:
        user_id = uuid.uuid4()
        new_user = user_schema.UserSchema(
            id=user_id, email="test@test.com", is_active=True)
        new_database_user = user_database.User(
            id=user_id, email="test@test.com", is_active=True)
        mock_module.get_user_by_email.return_value = None
        mock_module.create_user.return_value = new_database_user
        result = users.create_user(newUser=new_user, db=None)
        assert result.id == new_user.id
        assert result.email == new_user.email
        assert result.is_active == new_user.is_active


def test_create_user_exists():
    with mock.patch('app.routers.users.user', autospec=True) as mock_module:
        existing_user = user_database.User(
            id=uuid.uuid4(), email="test@test.com", is_active=True)
        new_user = user_schema.UserSchema(
            id=uuid.uuid4(), email="test@test.com", is_active=True)
        mock_module.get_user_by_email.return_value = existing_user
        with pytest.raises(fastapi.HTTPException):
            users.create_user(newUser=new_user, db=None)
