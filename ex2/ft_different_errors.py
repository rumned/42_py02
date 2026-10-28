#!/usr/bin/env python3
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 123
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    for i in range(5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except ValueError as ve:
            print(f"Caught ValueError: {ve}")
        except ZeroDivisionError as ze:
            print(f"Caught ZeroDivisionError: {ze}")
        except FileNotFoundError as fe:
            print(f"Caught FileNotFoundError: {fe}")
        except TypeError as te:
            print(f"Caught TypeError: {te}")
    print()
    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
