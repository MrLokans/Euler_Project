def main():
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                print("Largest palindrome is {} * {}, {}".format(i, j, product))
                exit(0)
if __name__ == '__main__':
    main()
