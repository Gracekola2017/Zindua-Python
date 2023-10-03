def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = int(num ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False
    return True

def prime_factors_in_range(i, n):
    factors = {}
    for num in range(i, n + 1):
        factors[num] = []
        for potential_factor in range(2, num + 1):
            if is_prime(potential_factor) and num % potential_factor == 0:
                factors[num].append(potential_factor)
    return factors

