import re
import sys

def get_python_version() -> str:
	return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def verify_student_output():
    """
    ^ asserts the start of the string.
    \\d+ matches one or more digits (the number).
    : matches the colon.
    matches a single space.
    (Heads|heads|Tails|tails) matches either "Heads," "heads," "Tails," or "tails."
    """
    pattern = r"^\d+: (Heads|heads|Tails|tails)$"

    test_cases = [
        "10:Heads",  # should fail because of lack of a space after :
        "5: Tails",  # should pass
        "42 :Heads",  # should fail because : is not up against the number
        "7:tails",  # should fail because of lack of a space after :
    ]

    for string in test_cases:
        match = re.match(pattern, string)
        print(f"{string}: {'Pass' if match else 'Fail'}")


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    verify_student_output()
