import math
from fractions import Fraction


class Calculate:

    @staticmethod
    def bernoulli_theorem(n, p, k):
        result = math.comb(n, k) * p ** k * (1 - p) ** (n - k)
        print(f'{math.comb(n, k)} · {p ** k} · {(1 - p) ** (n - k)}')
        return result

    @staticmethod
    def expectation(n, p):
        result = n * p
        print(f'{n} · {p}')
        return result

    @staticmethod
    def cumulative_probability(n, k, p):
        result = n * p * k
        return result

    @staticmethod
    def standard_deviation(n, p):
        result = math.sqrt(n * p * (1 - p))
        print(f'σ(X) = √ {n} · {p} · {(1 - p)}')
        return result


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
        def p():
            choose = int(input("Do you want to write p as a fraction (1) or decimal number (2)? "))

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
            result = Calculate.bernoulli_theorem(n, k, p)
        elif operation == 2:
            n = InputNumbers.n()
            p = InputNumbers.p()
            result = Calculate.expectation(n, p)
        elif operation == 3:
            n = InputNumbers.n()
            k = InputNumbers.k()
            p = InputNumbers.p()
            result = Calculate.cumulative_probability(n, k, p)
        else:
            n = InputNumbers.n()
            p = InputNumbers.p()
            result = Calculate.standard_deviation(n, p)

        return result

    except ValueError as value_err:
        print(value_err)


print(which_operation())
