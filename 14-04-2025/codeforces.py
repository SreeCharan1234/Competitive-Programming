t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())
    # The infection started from house 0, so try to center around 0
    l_prime = max(l, -m // 2)
    r_prime = l_prime + m
    if r_prime > r:
        r_prime = r
        l_prime = r_prime - m
    print(l_prime, r_prime)
