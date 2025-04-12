import pytest
from rpg_stats import *


@pytest.fixture
def average_character_stats():
    return {"strength": 5, "dexterity": 6}


def test_initial_strength():
    assert generate_strength() == 5


# def test_valid_stat_middle():
#     assert is_stat_valid(5) == True

# def test_valid_stat_lower_bound():
#     assert is_stat_valid(1) == True

# def test_valid_stat_upper_bound():
#     assert is_stat_valid(10) == True

# def test_invalid_stat_too_low():
#     assert is_stat_valid(0) == False

# def test_invalid_stat_too_high():
#     assert is_stat_valid(11) == False


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        (5, True),
        (1, True),
        (10, True),
        (0, False),
        (11, False),
    ],
)
def test_stat_validation(input_value, expected_value):
    assert is_stat_valid(input_value) == expected_value


def test_average_strength(average_character_stats):
    assert average_character_stats["strength"] == 5

def test_character_creation():
    hero = Character(5, 8, 6)
    assert hero.strength == 5
    assert hero.intelligence == 8

def test_character_combat_readiness():
    hero = Character(4, 9, 7)
    assert hero.get_combat_readiness() == 11