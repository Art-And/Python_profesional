import random

#using for
def remove_duplicates(some_list):
    without_duplicate = []

    for element in some_list:
        if element not in without_duplicate:
            without_duplicate.append(element)

    return without_duplicate

#using sets
def remove_duplicate_lists(my_list: list) -> list:
    return list(set(my_list))


def run():
    random_list = [random.randint(0,50) for _ in range(0,50)]
    print(len(random_list))
    remove_random_list = remove_duplicates(random_list)
    print(remove_random_list)
    print(len(remove_random_list))

if __name__ == '__main__':
    run()