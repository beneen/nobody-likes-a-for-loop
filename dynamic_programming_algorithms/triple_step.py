"""
-----
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs
-----
"""



def triple_step(steps):

    if steps <= 1:
        return 1
    if steps ==2:
        return steps
    return (triple_step(steps - 3) + triple_step(steps - 2) + triple_step(steps - 1))



def main():
    print(triple_step(int(input("insert number of stairs:"))))


if __name__ == "__main__":
    main()
