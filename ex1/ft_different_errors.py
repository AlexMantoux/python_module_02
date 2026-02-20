def garden_operations() -> None:
    """Demonstrate different types of errors that can occur
    in garden operations.

    This function contains operations that will raise different exceptions:
    ValueError, ZeroDivisionError, FileNotFoundError, and KeyError.
    It is intended to be called inside a try/except block.
    """
    int("qwe")

    10 / 0

    open("missing.txt", "r")

    dic = {"plant1": "rose", "plant2": "sunflower"}
    print(dic["missing_plant"])


def test_error_types() -> None:
    """Test and demonstrate different types of Python exceptions.

    Shows how to catch ValueError, ZeroDivisionError, FileNotFoundError,
    and KeyError separately, and how to catch multiple error types
    with a single except block. Demonstrates that the program
    continues running after each error.
    """
    print("=== Garden Error Types Demo ===")
    print()
    print("Testing ValueError...")
    try:
        int("qwe")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()
    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print()
    print("Testing KeyError...")
    try:
        dic = {"plant1": "rose", "plant2": "sunflower"}
        dic["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()
    print("Testing multiple errors together...")
    try:
        garden_operations()
    except (KeyError, FileNotFoundError, ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
