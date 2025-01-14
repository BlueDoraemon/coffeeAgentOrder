# tests/test_db_functions.py
import pytest
from unittest.mock import Mock, patch
import os
from db_access import DatabaseOperations, create_supabase_client

@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    """Mock environment variables for testing."""
    monkeypatch.setenv("SUPABASE_URL", "https://test-url.supabase.co")
    monkeypatch.setenv("SUPABASE_KEY", "test-key")

@pytest.fixture
def mock_supabase():
    """Create mock Supabase client."""
    mock_client = Mock()
    mock_client.table.return_value.select.return_value.execute.return_value = {
        'data': [
            {'id': 1, 'name': 'Espresso', 'price': 3.50},
            {'id': 2, 'name': 'Latte', 'price': 4.00}
        ]
    }
    return mock_client

@pytest.fixture
def db_ops(mock_supabase):
    """ mocked client."""
    return DatabaseOperations(mock_supabase)

def test_create_supabase_client():
    """Test Supabase client creation"""
    with patch('db_access.create_client') as mock_create:
        mock_create.return_value = Mock()
        client = create_supabase_client()
        assert client is not None

def test_create_supabase_client_failure():
    """Test Supabase client creation failure"""
    with patch('db_access.create_client', side_effect=ValueError("Connection failed")):
        client = create_supabase_client()
        assert client is None

def test_database_operations_init_failure():
    """Test DatabaseOperations initialisation with no client."""
    with patch('db_access.create_supabase_client', return_value=None):
        with pytest.raises(ValueError, match="Supabase client not initialized"):
            DatabaseOperations()

def test_get_coffees_success(db_ops, mock_supabase):
    """Test successful retrieval of coffee types."""
    result = db_ops.get_coffees()
    
    mock_supabase.table.assert_called_once_with("coffee_types")
    mock_supabase.table().select.assert_called_once_with("*")
    assert len(result) == 2
    assert result[0]['name'] == 'Espresso'
    assert result[1]['name'] == 'Latte'

def test_get_coffees_failure(db_ops, mock_supabase):
    """Test failed retrieval of coffee types."""
    mock_supabase.table.return_value.select.return_value.execute.side_effect = Exception("Database error")
    result = db_ops.get_coffees()
    assert result is None

def test_get_modifiers_success(db_ops, mock_supabase):
    """Test successful retrieval of modifiers."""
    mock_supabase.table.return_value.select.return_value.execute.return_value = {
        'data': [
            {'id': 1, 'name': 'Extra Shot', 'price': 0.50},
            {'id': 2, 'name': 'Syrup', 'price': 0.75}
        ]
    }
    
    result = db_ops.get_modifiers()
    
    mock_supabase.table.assert_called_once_with("modifiers")
    mock_supabase.table().select.assert_called_once_with("*")
    assert len(result) == 2
    assert result[0]['name'] == 'Extra Shot'
    assert result[1]['name'] == 'Syrup'

def test_get_modifiers_failure(db_ops, mock_supabase):
    """Test failed retrieval of modifiers."""
    mock_supabase.table.return_value.select.return_value.execute.side_effect = Exception("Database error")
    result = db_ops.get_modifiers()
    assert result is None
