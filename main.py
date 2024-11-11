import re


def verify_student_output():
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
    verify_student_output()