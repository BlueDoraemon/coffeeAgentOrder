import sys
import pytest
import os
from pathlib import Path

# add src to file path
src_path = Path(__file__).parent.parent / "src" / "fastAPI"
sys.path.append(str(src_path))

@pytest.fixture(autouse=True)
def mock_env_variables(monkeypatch):
    """Mock environment variables for testing."""
    monkeypatch.setenv("SUPABASE_URL", "https://test-url.supabase.co")
    monkeypatch.setenv("SUPABASE_KEY", "test-key")