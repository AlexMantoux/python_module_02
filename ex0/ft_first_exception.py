def check_temperature(temp_str: str) -> int | None:
    """Check if a temperature string is valid for plants.

    Takes a string input, converts it to an integer and checks
    if the temperature is within the acceptable range for plants
    (0 to 40 degrees Celsius).

    Args:
        temp_str: The temperature value as a string.

    Returns:
        The temperature as an integer if valid, None otherwise.
    """
    try:
        temp: int = int(temp_str)
        if (temp < 0):
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        elif (temp > 40):
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
        return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    """Test the check_temperature function with various inputs.

    Demonstrates normal operation, invalid input, and extreme
    values to show the program keeps running despite errors.
    """
    temp_values: list[str] = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===")
    print()
    for temp in temp_values:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
