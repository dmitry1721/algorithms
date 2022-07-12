"""
Даны целые числа 1 ≤ n ≤ 10^18 и 2 ≤ m ≤ 10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.

Sample Input:
10 2
Sample Output:
1
"""


def fib_mod(n, m):
    fib_list_mod = [0, 1]
    count = n
    if n > (6 * m):
        count = 6 * m
    for i in range(2, count+1):
        fib_list_mod.append(((fib_list_mod[i - 1] % m) + (fib_list_mod[i - 2] % m)) % m)
        if i >= 5:
            if fib_list_mod[i-2] == 0 and fib_list_mod[i-1] == 1 and fib_list_mod[i] == fib_list_mod[2]:
                result = fib_list_mod[:i-2][(n % len(fib_list_mod[:i-2]))]
                return result
    return fib_list_mod[len(fib_list_mod) - 1]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
