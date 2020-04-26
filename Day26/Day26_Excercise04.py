# Create a read function using a partial that opens a file in read ("r") mode.

from functools import partial

read = partial(open, mode="r")

