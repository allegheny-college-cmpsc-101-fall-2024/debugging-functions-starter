"""Calculate the absolute value (abs) of a number."""

# TODO: Find and fix any defect(s) inside of the abs function based on
# Guttag 8.1.2


def abs(x: int) -> int:
    """Assume x is an int.
       Returns x if x >= 0 and -x otherwise."""
    if x < -1:
        return -x
    else:
        return x


def test_abs() -> None:
    """Implement test cases for the is_prime function."""
    # test case: -2 should return 2
    input_negative = -2
    expected_output_negative = 2
    output_negative = abs(input_negative)
    if output_negative != expected_output_negative:
        print("Expected output not correct for a negative input!")
    else:
        print("Expected output correct for a negative input!")
    # TODO: Implement the remaining "test cases" as conditional
    # logic inside of this function
    # TODO: The "test cases" should produce output indicating
    # whether or not the function produced the expected output
    # TODO: test case: 2 should return 2
    # TODO: test case: -1 should return 1
    # TODO: test case: 1 should return 1


if __name__ == "__main__":
    test_abs()
