from dataclasses import dataclass


@dataclass(frozen=True)
class Constants:
    PI: float = 3.14


def main():
    constants = Constants()
    print(f"Initialized!! PI: {constants.PI}")
    constants.PI = "OVERWRITTEN"


if __name__ == "__main__":
    main()
