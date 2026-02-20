def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
        ) -> str:
    """Check if a plant's health parameters are within acceptable ranges.

    Args:
        plant_name: The name of the plant. Cannot be empty.
        water_level: The water level between 1 and 10.
        sunlight_hours: The sunlight hours between 2 and 12.

    Returns:
        A success message if all parameters are valid.

    Raises:
        ValueError: If plant_name is empty, water_level is out of
                    range, or sunlight_hours is out of range.
    """
    if (plant_name == ""):
        raise ValueError("Error: Plant name cannot be empty!")
    if (water_level < 1):
        raise ValueError(f"Error: Water level {water_level} "
                         "is too low (min 1)")
    if (water_level > 10):
        raise ValueError(f"Error: Water level {water_level} "
                         "is too high (max 10)")
    if (sunlight_hours < 2):
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too low (min 2)")
    if (sunlight_hours > 12):
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Test the check_plant_health function with various inputs.

    Demonstrates valid input, empty plant name, invalid water level,
    and invalid sunlight hours, showing how errors are raised and caught.
    """
    plant_name: str = "tomato"
    water_level: int = 7
    sunlight_hours: int = 8

    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    try:
        print(check_plant_health(plant_name, water_level, sunlight_hours))
    except ValueError as e:
        print(f"{e}")
    print()
    print("Testing empty plant name...")
    try:
        plant_name = ""
        print(check_plant_health(plant_name, water_level, sunlight_hours))
    except ValueError as e:
        print(f"{e}")
    print()
    print("Testing bad water level...")
    try:
        plant_name: str = "tomato"
        water_level: int = 15
        sunlight_hours: int = 8
        print(check_plant_health(plant_name, water_level, sunlight_hours))
    except ValueError as e:
        print(f"{e}")
    print()
    print("Testing bad sunlight hours...")
    try:
        water_level: int = 7
        sunlight_hours: int = 0
        print(check_plant_health(plant_name, water_level, sunlight_hours))
    except ValueError as e:
        print(f"{e}")
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
