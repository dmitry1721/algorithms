"""
Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи (напомним, что F_0=0, F_1=1
и F_n = F_{n-1} + F_{n-2} при n ≥ 2).

Sample Input:
3
Sample Output:
2
"""


def fib(n):
    fib_list = [1] * n
    for i in range(2, n):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[n-1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
