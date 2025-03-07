# Constant with Python

This repository contains examples of how to define constants in Python without mypy.

## Description

Python is a dynamically typed language, which means that the type of a variable is determined at runtime. This means that you can change the type of a variable at any time. However, there are some values that are constant which means they cannot be changed.

```python
PI = 3.14
```

Usually, constants are written in uppercase letters. But, in this way, you can still change the value of the constant.

```python
from typing import Final

PI: Final[int] = 3.14
PI = "OVERWRITTEN" # This will raise an error
```

However, sometimes we can not use mypy because of organizational reasons. We introduce another way to define constants in Python.

## Usage

You can run the following command to see the output:

```shell
python reassign_class.py
# uv run reassign_class.py, just class

python reassign_dataclass.py
# uv run reassign_dataclass.py, just dataclass

python reassign_enum.py
# uv run reassign_enum.py, just enum

python reassign_slots.py
# uv run reassign_slots.py, just slots
```

## License

This repository is under the [MIT License](./LICENSE).

## Contribution

Feel free to contribute to this repository. For example, you can add new examples or improve the existing ones. Just open a pull request and I will review it as soon as possible.

Check the code style with the following command:

```shell
uv run black .
```
