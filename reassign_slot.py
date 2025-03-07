class Constants:
    __slots__ = "_pi"

    def __init__(self):
        self._pi = 3.14

    @property
    def PI(self):
        return self._pi


def main():
    constants = Constants()
    print(f"Initialized!! PI: {constants.PI}")
    constants.PI = "OVERWRITTEN"


if __name__ == "__main__":
    main()
