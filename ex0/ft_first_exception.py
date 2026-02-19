def check_temperature(temp_str: str) -> None:
    try:
        temp: int = int(temp_str)
        if (temp < 0):
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif (temp > 40):
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    temp_values: list[str] = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===")
    print()
    for temp in temp_values:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
        print()
    print("All tests completed - program didn't crash!")
