#!/usr/bin/env python3

import sys
import signal

def factorize(n):
    factors = []
    # Start from 2 and iterate up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If i divides n, add i and n//i to factors
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is prime and greater than 1, add n to factors
    if n > 1:
        factors.append(n)
    return factors

def handler(signum, frame):
    print("Time limit exceeded. Exiting.")
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: ./factors.py <file>")
        sys.exit(1)

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(15)  # Set a timeout of 15 seconds

    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            for line in file:
                n = int(line.strip())
                factors = factorize(n)
                # Output factorization in the format "n=p*q"
                print(f"{n}={'*'.join(map(str, factors))}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Keyboard interrupt. Exiting.")
        sys.exit(1)
    finally:
        signal.alarm(0)  # Disable the timeout

if __name__ == "__main__":
    main()
