import random

l = [random.randint(1, 100) for i in range(20)]
print(l)


def main():
    def get_max(l):
        max_1 = l[0]
        for items in l:
            if items > max_1:
                max_1 = items
        return max_1

    max_2 = get_max(l)
    print("Max:", max_2)
    pass

    def get_min(l):
        min_1 = l[0]
        for items in l:
            if items < min_1:
                min_1 = items
        return min_1

    min_2 = get_min(l)
    print("Min:", min_2)
    pass

    def get_avg(l):
        return sum(l) / len(l)

    avg = get_avg(l)
    print("AVG:", avg)
    pass

    def sum_even(l):
        even = []
        for i in l:
            if i % 2 != 1:
                even.append(i)
        print("Even list:", even)
        return sum(even)
    print("Sum even:", sum_even(l))
    pass

    def sum_odd(l):
        odd = []
        for i in l:
            if i % 2 != 0:
                odd.append(i)
        print("Odd list:", odd)
        return sum(odd)
    print("Sum odd:", sum_odd(l))
    pass

    def get_factorial(l):
        result = 1
        for i in l:
            result = result * i
        return result
    print("Result of l: ", get_factorial(l))
    pass


if __name__ == "__main__":
    main()
