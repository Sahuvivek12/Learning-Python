import functools
import time


@functools.lru_cache(maxsize=None)
def fac(n):
    if (n == 0 or n == 1):
        return 1
    time.sleep(2)
    return n * fac(n-1)

print(fac(3))
print(fac(4))
print(fac(5))

print(fac(3))
print(fac(4))
print(fac(5))
