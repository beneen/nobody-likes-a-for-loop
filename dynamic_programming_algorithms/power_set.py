"""
-----
Write a method to return all subsets of a set.
-----
"""
from functools import reduce

def all_subsets(set):
        return reduce(lambda rolling_window_over_set, x: rolling_window_over_set + [rest_of_set_being_passed_over + [x] for rest_of_set_being_passed_over in rolling_window_over_set], set, [[]])

def main():
    print(all_subsets(set(input("set:"))))


if __name__ == "__main__":
    main()
