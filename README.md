
# Debugging Functions

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-blue.svg)](https://github.com/psf/black)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Discord](https://img.shields.io/discord/872320492936257537?logo=discord)](https://discord.gg/kjah8MFYbR)

## Introduction

This assignment invites you to learn more about the debugging and testing
process described in Guttag Chapter 8 by running and observing two Python
programs called `perform-primality-check` and `perform-abs-computation`.

## Learning Objectives

The learning objectives of this assignment are to:

1. Use Git and GitHub to manage source code file changes
2. Write simple tests with print statements in python source code
3. Correct bugs in python source code
4. Write clearly about the programming concepts in this assignment.

## Quick Links

- Due date: Check Discord or the
  [Course Materials Schedule](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials/blob/main/Schedule.md)
- Policy on
  [Tokens](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#tokens)
- [Token Form for Automatic Extension](https://forms.gle/y9Mz55hQKr84wzvXA)
- Policy for
  [Assignment Evaluation](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#assignment-evaluation)
- Policy for [Assignment Submission](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#assignment-submission).
- [#data-structures Discord channel](https://discord.com/channels/877320365825749002/1274744318124359732)
- [Starter repo](https://github.com/allegheny-college-cmpsc-101-fall-2024/debugging-functions-starter)

## Policy Reminders

Students are reminded to uphold the Honor Code. Cloning this assignment
repository is a commitment to the latter.

For this assignment, you may use class materials, the textbook, notes,
and the internet, including AI, for reference and learning. AI may **not** be
used to generate answers that you submit. All code and writing that are turned
in **must be your own work and your own words**. Copying or otherwise
representing ChatGTP or other AI outputs as your own work or your own words is
not permitted.

Please ask questions freely in Lab, on the #data-structures Discord channel,
TL office hours, instructor office hours, or by opening a GitHub Issue with
@emgraber tagged at least 24 hours before the deadline.

Modifications to the gatorgrade.yml file are not permitted without explicit
instruction.

## Project Details (Overview Below)

This assignment invites you to run and observe two Python programs called
`perform-primality-check` and `perform-abs-computation`. Instead of using the
[Poetry](https://python-poetry.org/) tool for managing dependencies and
packaging these programs, these programs are scripts, without any dependencies
on other Python packages, that you can run through the Python interpreter.
As you continue to practice a different way to run a Python program, this
project offers you the opportunity to improve your understanding of how to
debug and test Python functions that have a defect inside of them. Specifically
you will write test cases that:

- (i) create an input for a function
- (ii) pass that input to the function under test
- (iii) capture the output of the function under test
- (iv) assert that the captured function output equals the expected output if
  the function was implemented correctly.
  
Instead of using a test automation framework to run these tests you will organize
them into functions in the same module as the function under test.

### Code Survey and Expected Output

If you change into the `source/` directory of your GitHub repository, you will
see two Python files called `perform-primality-check.py` and
`perform-abs-computation.py`. The `perform-primality-check` module contains a
defective function with the signature `def is_prime(x: int) -> bool`. Your task
is to identify and fix the defects inside of this function! To aid your
debugging efforts, you should use and extend the `def test_is_prime() -> None`
function that should subject the `is_prime` function to several tests. The first
test in the `test_is_prime` is implemented in the following fashion:

```python linenums="1"
def test_is_prime() -> None:
    """Implement test cases for the is_prime function."""
    input_zero = 0
    expected_output_zero = False
    output_zero = is_prime(input_zero)
    if output_zero is not expected_output_zero:
        print("Expected output not correct for input of zero!")
    else:
        print("Expected output correct for input of zero!")
```

In the first part of this function, line `3` indicates that the test will input
the value of `0` to the `is_prime` function and line `4` shows that the expected
output of `is_prime` for this input is `False` because `0` is not a prime
number. Line `5` of this function calls the `is_prime` function with the
previously constructed input and then lines `6` through `9` provide some
diagnostic output that explains whether or not the output was correct.
Specifically, if the actual output from the function is not equal to the
expected output, then line `7` displays a message indicating that the output is
not correct. When the expected output is equal to `is_prime`'s actual output,
then line `9` displays a message revealing that the function works correctly.
Even though this test does not use a specific test automation framework it
illustrates the key steps that a test case should take to both find defects and
establish a confidence in the correctness of `is_prime`.

After adding more test cases to the `perform-primality-check` module, you should
follow the same process when you debug and test the `abs` function in the
`perform-abs-computation` module. Ultimately, you should ensure that both of the
defective functions no longer have defects inside of them! For instance, when
the test cases for the `is_prime` function are passing correctly they should
produce the following output:

```
Expected output correct for input of zero!
Expected output correct for input of one!
Expected output correct for input of two!
Expected output correct for input of forty-one!
```

### Running Checks

Since this project does not use [Poetry](https://python-poetry.org/) to manage
project dependencies and virtual environments, it does not support the use of
commands like `poetry run task test`.

### Gatorgrade

After you have added functionality and checked that your code produces the
expected output, the command `gatorgrade --config config/gatorgrade.yml`
will check your work with the automatic grader. If
your work meets the baseline requirements and adheres to the best practices that
proactive programmers adopt you will see that all the checks pass when you run
`gatorgrade`. All checks must pass in order to get 100% on this lab. All other
gatorgrade score are graded as 0%. Note, modifications to the gatorgrade.yml
file are not permitted without explicit instruction.

### Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file.
Please provide output from running each of the
provided Python programs on your own laptop and then explain how the program's
source code produced that output. A specific goal for this project is to ensure
that you can explain each defect that you found in the function and how the test
cases that you implemented helped you to find it. You should also reflect on how
the tests that you created as part of this source code survey are similar to and
different from the ones you might create with a framework like
[Pytest](https://docs.pytest.org/). Finally, make sure that you take time to
think through the strategy you have adopted for debugging Python functions,
further considering the ways in which you can improve it.

## Project Overview

After cloning this repository to your computer, please take the following
steps:

- Change into the program source code directory by typing `cd source`.
- Run both of the provided Python scripts by typing the following:
  - `python perform_primality_check.py`: perform checks for number primality
  - `python perform_abs_computation.py`: perform the absolute value computation
- Make sure that you fix the defects inside of these programs!
- Confirm that the programs are producing the expected output.
- Make sure that you can explain why the programs produce the output that they do.
- Run the automated grading checks by typing
  `gatorgrade --config config/gatorgrade.yml`.  
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all of the required responses to the technical writing
  prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
  labels from all of the provided source code.
- Please make sure that you also completely delete the `TODO` markers and their
  labels from every line of the `writing/reflection.md` file.
- Submit work to GitHub using git in the terminal
  - Open a terminal
  - `cd` to the project directory on your computer
  - type `git status` to see a list of files you have updated
  - type `git add .` to "stage" your files
  - type `git commit -m "PUT YOUR OWN SHORT MESSAGE"`
  - type `git push origin main`
  - type your ssh passphrase if requested
