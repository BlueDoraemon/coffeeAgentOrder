import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_supabase():
    with patch('your_module.supabase') as mock_client:
        yield mock_client

def test_get_coffees(mock_supabase):
    mock_response = MagicMock()
    mock_response.data = [
        {"id": 1, "name": "Espresso"},
        {"id": 2, "name": "Latte"}
    ]

mock_supabase.table.return_value.select.return_value.execute.return_value = mock_response

from your_module import get_coffees
response = get_coffees()

assert response.data == mock_response.data
mock_supabase.table.assert_called_once_with("coffee_types")
mock_supabase.table.return_value.select.assert_called_once_with("*")

def test_get_modifiers():
    from your_module import get_modifiers
    assert get_modifiers() == NotImplemented

def test_add_coffee():
    from your_module import add_coffee
    assert add_coffee() == NotImplemented

def test_add_order():
    from your_module import add_order
    assert add_order() == NotImplemented

def test_get_orders():
    from your_module import get_orders
    assert get_orders() == NotImplemented

@pytest.fixture
def mock_env_vars():
    with patch.dict('os.environ', {
        'SUPABASE_URL': 'https://example.supabase.co',
        'SUPABASE_KEY': 'your-supabase-key'
    }):
        yield

def test_supabase_client_initialization(mock_env_vars):
    with patch('your_module.create_client') as mock_create_client:
        from your_module import supabase

        mock_create_client.assert_called_once_with(
            'https://example.supabase.co',
            'your-supabase-key',
            options=ClientOptions(
                postgrest_client_timeout=10,
                storage_client_timeout=10,
                schema="public"
            )
        )