from food_and_drinks import calculate


def test_calculate_food_and_drinks_for_one_person():
    expected_food_and_drinks = "1 pizza and 2 orange juices."

    assert calculate(1) == expected_food_and_drinks


def test_calculate_food_and_drinks_for_ten_persons():
    expected_food_and_drinks = "1 pizza and 20 orange juices."

    assert calculate(10) == expected_food_and_drinks


def test_calculate_food_and_drinks_for_twenty_persons():
    expected_food_and_drinks = "2 pizzas and 40 orange juices."

    assert calculate(20) == expected_food_and_drinks


def test_calculate_food_and_drinks_for_one_hundred_persons():
    expected_food_and_drinks = "8 pizzas and 160 orange juices."

    assert calculate(100) == expected_food_and_drinks
