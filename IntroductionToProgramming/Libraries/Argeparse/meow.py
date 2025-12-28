# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _n in range(n):
#         print("meow")
# else:
#     print("usuage: meows.py")

"""
This program prints "meow" a specified number of times.

Earlier, this functionality was implemented using `sys.argv`, which required
manual length checks and index-based access to arguments. That approach becomes
harder to read and maintain as the number of arguments grows.

Here, we use the `argparse` module instead, which provides:
- Cleaner and more readable code
- Automatic argument parsing and validation
- Built-in help and error messages
- Better scalability for command-line tools
"""

import argparse

parser = argparse.ArgumentParser(description="Print 'meow' multiple times")
parser.add_argument(
    "-n",
    type=int,
    required=True,
    help="Number of times to print 'meow'"
)

args = parser.parse_args()

for _ in range(args.n):
    print("meow")
