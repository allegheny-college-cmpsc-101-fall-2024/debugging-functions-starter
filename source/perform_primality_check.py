"""Determine if specific numbers are or are not prime numbers."""

# TODO: Find and fix any defect(s) in the is_prime function, based on
# Guttag 8.1.2


def is_prime(x: int) -> bool:
    """Assume x is a non-negative int.
       Returns True if x is prime; False otherwise."""
    if x <= 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def test_is_prime() -> None:
    """Implement test cases for the is_prime function."""
    # test case: 0 is not a prime number
    input_zero = 0
    expected_output_zero = False
    output_zero = is_prime(input_zero)
    if output_zero is not expected_output_zero:
        print("Expected output not correct for input of zero!")
    else:
        print("Expected output correct for input of zero!")
    # TODO: Implement the remaining "test cases" as conditional
    # logic inside of this function
    # TODO: The "test cases" should produce output indicating
    # whether or not the function produced the expected output
    # TODO: test case: 1 is not a prime number
    # TODO: test case: 2 is a prime number
    # TODO: test case: 41 is a prime number


if __name__ == "__main__":
    test_is_prime()
