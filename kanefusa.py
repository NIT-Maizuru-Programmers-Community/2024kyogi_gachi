import random

def generate_random_lists(n):
    random_lists = []
    empty_list=[]
    for _ in range(n):
        size = random.randint(1, 3)
        first_row = [random.randint(0, 1) for _ in range(size)]
        second_row = [0] * size  # 2行目はすべて0
        random_lists.append([first_row, second_row])
    return random_lists


