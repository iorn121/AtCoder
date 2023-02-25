#! /usr/bin/env python3
import random


def main():
    N = random.randint(1, 10)
    K = random.randint(0, N)
    S = [random.choice(["X", "Y"]) for _ in range(N)]

    print(N, K)
    print("".join(S))


if __name__ == "__main__":
    main()
