"""
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?
"""


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def main():
    answer = 1
    for i in range(1, 11):
        print("-"*30)
        print("Iteration: {}".format(i))
        print("GCD: {}".format(gcd(i, answer)))
        print("Answer before computation: {}".format(answer))
        print("Iteration: {}".format(i))
        answer *= i // gcd(i, answer)
        print("Answer after computation: {}".format(answer))
    print(answer)

if __name__ == '__main__':
    main()
