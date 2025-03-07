class Constants:
    def __init__(self):
        self._constants = {}

    def __setattr__(self, name, value):
        if name == "_constants":
            super().__setattr__(name, value)
            return

        if name in self._constants:
            raise TypeError(f"Can not overwrite constant: {name}")

        self._constants[name] = True
        super().__setattr__(name, value)


def main():
    constants = Constants()
    constants.PI = 3.14
    print(f"Initialized!! PI: {constants.PI}")
    constants.PI = "OVERWRITTEN"


if __name__ == "__main__":
    main()
