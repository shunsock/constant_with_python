from enum import Enum, auto


class Constants(Enum):
    PI = 3.14


def main():
    print(f"Initialized!! PI: {Constants.PI.value}")
    Constants.PI = "OVERWRITTEN"


if __name__ == "__main__":
    main()
