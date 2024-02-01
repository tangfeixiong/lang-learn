#!/usr/bin/env python3

"""https://www.geeksforgeeks.org/zip-in-python/"""

def with_list() -> None:
    name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
    roll_no = [4, 1, 3, 2]

    # using zip() to map values
    mapped = zip(name, roll_no)
    print(set(mapped))

def with_enumerate() -> None:
    names = ['Nukesh', 'Roni', 'Chari']
    ages = [20, 50, 18]

    for i, (name, age) in enumerate(zip(names, ages)):
        print(i, name, age)

def with_dictionary() -> None:
    stocks = ['GEEKS', 'For', 'geeks']
    prices = [2175, 1127, 2750]

    new_dict = {stock: price for stock, price in zip(stocks, prices)}
    print(new_dict)

def with_tuple() -> None:
    tuple1 = (1, 2, 3)
    tuple2 = ('a', 'b', 'c')
    zipped = zip(tuple1, tuple2)
    result = list(zipped)
    print(result)

def with_multiple_iterables() -> None:
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = ['x', 'y', 'z']
    zipped = zip(list1, list2, list3)
    result = list(zipped)
    print(result)

def with_unequal_size() -> None:
    # Define lists of 'persons', 'genders', and a tuple for 'ages'
    persons = ["Chandler", "Monica", "Ross", "Rachel", "Joey", "Phoebe", "Joanna"]
    genders = ["Male", "Female", "Male", "Female", "Male", "Female", "Female"]
    ages = (35, 36, 38, 34)

    # Create a zipped object combining the 'persons' and 'genders' list along with 'ages' tuple
    zipped_result = zip(persons, genders, ages)

    # Print the zipped object
    print("Zipped result as a list:")
    for i in list(zipped_result):
        print(i)

def unzipping_with() -> None:
    # initializing lists
    name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
    roll_no = [4, 1, 3, 2]
    marks = [40, 50, 60, 70]

    # using zip() to map value
    mapped = zip(name, roll_no, marks)

    # converting values t print as list
    mapped = list(mapped)

    # printing resultant values
    print("The zipped result is : ", end="")
    print(mapped)

    print("\n")

    # unzipping values
    namz, roll_noz, markz = zip(*mapped)

    print("The unzipped result: \n", end="")

    # printing initial lists
    print("The name list is  : ", end="")
    print(namz)

    print("The roll_no list is : ", end="")
    print(roll_noz)

    print("The marks list is : ", end="")
    print(markz)
 
def with_loops() -> None:
    # Python code to demostrate the application of zip()

    # initializing list of players.
    players = ["Sachin", "Sehwg", "Gambhir", "Dravid", "Raina"]

    # initializing their scores
    scores = [100, 15, 17, 28, 43]

    # printing players and scores
    for pl, sc in zip(players, scores):
        print("Player : %s    Scores : %d" % (pl, sc))


if __name__ == "__main__":
    with_list()
    with_enumerate()
    with_dictionary()
    with_tuple()
    with_multiple_iterables()
    with_unequal_size()
    unzipping_with()
    with_loops()


