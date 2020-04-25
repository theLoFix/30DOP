# Use the sample function in the random module to create three lists, each containing fifteen numbers from 1 to 100 (inclusive). Sort each of these lists into descending order (largest first), and then truncate each list so that only 5 items remain in each
from random import sample

def create_list():
    random_list = sample(range(1,101), 15)
    random_list.sort(reverse=True)
    del random_list[5:]
    return random_list

lists = [create_list() for _ in range(3)]

print(*lists,sep="\n")