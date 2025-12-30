import os
import pytest
from app.db.database import Database

@pytest.fixture
def in_memory_db():
    """
    Fixture to provide an in-memory database for testing.
    """
    db = Database(":memory:")
    yield db
    db.close()

def test_database_connection(in_memory_db):
    query = '''
        SELECT * FROM activities;
    '''
    result = in_memory_db.cursor.execute(query)
    assert result is not None

def test_database_setup(in_memory_db):
    queries = [
        "SELECT name FROM sqlite_master WHERE type='table' AND name='activities'",
        "SELECT name FROM sqlite_master WHERE type='table' AND name='focus'",
        "SELECT name FROM sqlite_master WHERE type='table' AND name='focus_loss'"
    ]
    for query in queries:
        result = in_memory_db.cursor.execute(query)
        assert result.fetchone() is not None
