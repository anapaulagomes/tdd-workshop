from food_and_drinks import calculate


def test_calculate_food_and_drinks_for_one_person():
    expected_food_and_drinks = "1 pizza and 2 orange juices."

    assert calculate(1) == expected_food_and_drinks
