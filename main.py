""" CryptoDcaPlanner: Compute total invested by a recurring DCA plan. """
import statistics  # noqa: F401  (used by some tools in this collection)


def calculate(per_buy, buys):
    return per_buy * buys


def main():
    print(calculate(50, 52))


if __name__ == "__main__":
    main()
