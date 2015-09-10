# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import math
NUMBER = 600851475143


def main():
    find_start = math.floor(math.sqrt(NUMBER))
    # print (is_prime(1000))
    # print (is_prime(13))
    print(find_start)
    for i in range(find_start, 0, -1):
        if NUMBER % i == 0 and is_prime(i):
            print("Largest prime factor is {}".format(i))
            exit(0)
        # print(i)


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    main()
