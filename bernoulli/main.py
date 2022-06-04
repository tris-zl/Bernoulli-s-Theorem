import math
from fractions import Fraction

try:
    n = int(input("Type in the length of the Bernoulli chain (n ∈ ℕ): "))
    if n < 0:
        print("please note that n must be a natural number")
        exit()

    k = int(input("Type in the number of favorable outcomes (k ∈ ℕ): "))
    if k < 0:
        print("Please note that k must be a natural number...")
        exit()

    chooseP = int(input("Do you want to write p as a fraction (1) or decimal number (2)? "))
    if chooseP == 1:
        numerator = int(input("Type in the numerator (numerator ∈ ℤ): "))
        denominator = int(input("Type in the denominator (denominator ∈ ℤ)  "))
        p = float(Fraction(numerator/denominator))
    elif chooseP == 2:
        p = float(input("What's the probability of a favorable outcome? (0 < p < 1) "))
        if p > 1 or p < 0:
            print("Please note that p must be in between 0 and 1...")
            exit()
    else:
        print("Please give a legal response: ")
        exit()

    result = math.comb(n, k) * p ** k * (1-p) ** (n-k)
    print(f'P(X={k}) = {math.comb(n, k)} * {p ** k} * {(1-p) ** (n-k)} = {result} = {result * 100}%')

except ValueError as value_err:
    print(value_err)

except NameError as name_err:
    print(name_err)
