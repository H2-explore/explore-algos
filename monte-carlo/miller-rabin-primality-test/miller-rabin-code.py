import secrets

def is_probable_prime(n: int, k: int = 5) -> bool:
    # Return True if n is probably prime using k rounds of Miller-Rabin
    if n < 2:
        return False
    if n in (2,3):
        return True
    if n % 2 == 0:
        return False
    
    # write n-1 as 2^r * d with d odd
    d = n-1
    r = 0
    while d % 2 == 0:
        d //=2
        r+=1

    for _ in range(k):
        a = secrets.randbelow(n-3)+2 # random a in [2,n-2]
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True


if __name__ == "__main__":
    test_numbers = [2, 3, 4, 15, 17, 561, 1105, 170141183460469231731687303715884105727]
    for num in test_numbers:
        print(f"{num}: {'prime' if is_probable_prime(num, k=8) else 'composite'}")