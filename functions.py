#from re import L


def increment(number: int, by: int) -> int:
    """increment function value by second param"""
    return number + by


def multiply(*list) -> tuple:
    """gets to multiply a turple input"""
    total = 1
    for number in list:
        total *= number
    return total


def save_user(**user):
    print(user)


save_user(id=1, name="Simon")

print(increment(2, 5))

print(multiply(2, 4, 5, 2))
