"""
Let's say your company is hosting the next PyLadies meetup.
One of your tasks is calculating how much food and drinks
would be needed to buy.

Somebody told you that you should go for 1 pizza
for every 10 people who RSVPed and 2 orange juices
per person. You already know that 20% of the RSVPs
usually don't show up. This number should be included
in your calculations as well if the number of RSVPs is
greater than 20.

Your method `calculate()` should receive the number of
RSVPs and calculate food and drinks for the meetup.
"""
import math


def calculate(persons):
    no_show_rate = 0.2
    pizzas = persons // 10
    pizzas = 1 if pizzas == 0 else pizzas
    juices = 2 * persons

    if persons > 20:
        pizzas = math.trunc(pizzas - (pizzas * no_show_rate))
        juices = math.trunc(juices - (juices * no_show_rate))

    pizza_label = "pizzas" if pizzas > 1 else "pizza"
    juice_label = "juices" if juices > 1 else "juice"
    return f"{pizzas} {pizza_label} and {juices} orange {juice_label}."
