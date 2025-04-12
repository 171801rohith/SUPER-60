from idlelib.pathbrowser import PathBrowser
from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
from cards_proj.src import cards


@pytest.fixture
def sample_data():
    return [1, 2, 3]


@pytest.fixture
def base_number():
    return 5


@pytest.fixture
def square_number(base_number):
    return base_number**2


@pytest.fixture
def some_data():
    return 43


@pytest.fixture
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


@pytest.fixture
def greet():
    return "Hello"


@pytest.fixture
def user_data():
    return {"name": "ABC", "age": 33}


def test_sum(sample_data):
    assert sum(sample_data) == 6


def test_square(square_number):
    assert square_number == 25


def test_some_data(some_data):
    assert some_data == 43


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    assert cards_db.add_card(cards.Card("First"))
    assert cards_db.add_card(cards.Card("Second"))
    assert cards_db.add_card(cards.Card("Third"))


def test_function(greet):
    assert greet == "Hello"


def test_user(user_data):
    assert user_data["name"] == "ABC"
