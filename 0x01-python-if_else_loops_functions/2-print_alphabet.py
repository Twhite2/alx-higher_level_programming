#!/usr/bin/python3
"""
Print the alphabet in lowercase using ASCII, not followed by a new line.
"""

for i in range(97, 123):
    print("{:c}".format(i), end="")
