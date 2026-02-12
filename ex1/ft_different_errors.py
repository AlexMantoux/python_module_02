def garden_operations() -> None:
    int("qwe")

    res = 10 / 0

    open("missing.txt", "r")

    dic = {"key1": 1, "key2": 2}
    dic["missing_plant"]

def test_error_types() -> None:
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
        res : int = 10 / 0
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
    print("All error types tested successfully!")
