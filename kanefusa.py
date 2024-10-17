import random

def generate_random_lists(n):
    random_lists = []
    for _ in range(n):
        size_x = random.randint(1, 256)
        size_y = random.randint(1, 256)
        random_one=[]
        for y in range(0,size_y):
            row = [random.randint(0, 1) for _ in range(size_x)]
            random_one.append(row)
        random_lists.append(random_one) 

    return random_lists

#print(generate_random_lists(3))