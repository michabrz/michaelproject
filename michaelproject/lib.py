def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum


if __name__ == "__main__":
    # list with numbers
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    enum = is_even_num(l)
    print(enum)
