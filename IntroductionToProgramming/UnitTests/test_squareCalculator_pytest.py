
from squareCalculator import square

''' In the approach shown below, we wrote many lines of code just to test a very simple function.
This is not ideal because the test code becomes longer and harder to maintain compared to the
actual logic we are trying to verify. '''

# def main():
#     test_square()
#
# def test_square():
#     if square(2) != 4:
#         print("Square of 2 is not equal to 4")
#     if square(3) != 9:
#         print("Square of 3 is not equal to 9")
#     if square(-3) != 9:
#         print("Square of -3 is not equal to 9")
#
# if __name__ == "__main__":
#     main()


'''To improve this, we can use *pytest*, which provides a cleaner way to write and run tests.
With pytest, each test is simply an assert statement.'''

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

'''However, even this approach has a limitation:
If one assertion fails, pytest stops running the *rest of the asserts inside the same function*.
This means you may not see all failures clearly.

To solve this, we separate our tests into multiple test functions:'''

import pytest


def test_positives():
    assert square(2) == 4
    assert square(3) == 9

def test_negatives():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    # Verify that passing a string raises an error
    with pytest.raises(TypeError):
        square("cat")

'''This separation makes pytest run each function as an independent test,
producing cleaner and easier-to-read output.'''


'''Even with pytest, some learners may find the output format less readable at first.
Python also provides a built-in testing framework called `unittest`,
which offers a more structured and descriptive test output. 
'''