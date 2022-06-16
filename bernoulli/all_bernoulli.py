import math
from fractions import Fraction


class Calculate:

    @staticmethod
    def bernoulli_theorem(n, k, p):
        result = math.comb(n, k) * p ** k * (1 - p) ** (n - k)
        print(f'\nP(X) = {math.comb(n, k)} · {p ** k} · {(1 - p) ** (n - k)} = {result} = {result * 100} %')

    @staticmethod
    def expectation(n, p):
        result = n * p
        print(f'\nE(X) = {n} · {p} = {result}')

    @staticmethod
    def cumulative_probability(n, k, p, x):
        result = 0
        if x == 1:
            for i in range(0, k + 1):
                one_k = math.comb(n, i) * p ** i * (1 - p) ** (n - i)
                result = result + one_k
            print(f'\nP(X ≤ {k}) = {result} = {result * 100} %')
        elif x == 2:
            for i in range(k, n + 1):
                one_k = math.comb(n, i) * p ** i * (1 - p) ** (n - i)
                result = result + one_k
            print(f'\nP(X ≥ {k}) = {result} = {result * 100} %')
        elif x == 3:
            k2 = InputNumbers.k2()
            for i in range(k, k2 + 1):
                one_k = math.comb(n, i) * p ** i * (1 - p) ** (n - i)
                result = result + one_k
            print(f'\nP({k} ≤ X ≤ {k2}) = {result} = {result * 100} %')
        else:
            print("invalid enter")

    @staticmethod
    def standard_deviation(n, p):
        result = math.sqrt(n * p * (1 - p))
        print(f'\nσ(X) = √ {n} · {p} · {(1 - p)} = {result}')


class InputNumbers:

    try:
        @staticmethod
        def n():
            n = int(input("Type in the length of the Bernoulli chain (n ∈ ℕ): "))
            if n < 0:
                print("please note that n must be a natural number")
                exit()
            return n

        @staticmethod
        def k():
            k = int(input("Type in the number of favorable outcomes (k ∈ ℕ): "))
            if k < 0:
                print("Please note that k must be a natural number...")
                exit()
            return k

        @staticmethod
        def k2():
            k2 = int(input("Type in the number of favorable outcomes (Your second k number) (k ∈ ℕ): "))
            if k2 < 0:
                print("Please note that k must be a natural number...")
                exit()
            return k2

        @staticmethod
        def p():
            choose = int(input("Do you want to write p as a fraction (1) or decimal number (2)? "))

            p = 0
            if choose == 1:
                numerator = int(input("Type in the numerator (numerator ∈ ℤ): "))
                denominator = int(input("Type in the denominator (denominator ∈ ℤ)  "))
                p = float(Fraction(numerator / denominator))
            elif choose == 2:
                p = float(input("What's the probability of a favorable outcome? (0 < p < 1) "))
                if p > 1 or p < 0:
                    print("Please note that p must be in between 0 and 1...")
                    exit()
            else:
                print("Please give a legal response: ")
                exit()

            return p

        @staticmethod
        def x():
            choose = int(input("Choose from 'x ≤ k' (1), 'x ≥ k' (2) or 'k ≤ x ≤ k' (3)"))
            return choose

    except ValueError as value_err:
        print(value_err)


def which_operation():
    try:
        operation = int(input("Select one of the listed mathematical operations.\n"
                              "1 = bernoulli's theorem\n"
                              "2 = expectation\n"
                              "3 = cumulative probability\n"
                              "4 = standard deviation\n"))
        if operation == 1:
            n = InputNumbers.n()
            k = InputNumbers.k()
            p = InputNumbers.p()
            Calculate.bernoulli_theorem(n, k, p)
        elif operation == 2:
            n = InputNumbers.n()
            p = InputNumbers.p()
            Calculate.expectation(n, p)
        elif operation == 3:
            x = InputNumbers.x()
            n = InputNumbers.n()
            k = InputNumbers.k()
            p = InputNumbers.p()
            Calculate.cumulative_probability(n, k, p, x)
        elif operation == 4:
            n = InputNumbers.n()
            p = InputNumbers.p()
            Calculate.standard_deviation(n, p)
        else:
            print('invalid enter')
            exit()

    except ValueError as value_err:
        print(value_err)


which_operation()
