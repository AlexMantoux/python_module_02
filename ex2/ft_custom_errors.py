class GardenError(Exception):
    """A basic error for garden problems."""
    pass


class PlantError(GardenError):
    """For problems with plants."""
    pass


class WaterError(GardenError):
    """For problems with watering."""
    pass


def test_raising_errors() -> None:
    """Test and demonstrate custom garden exception classes.

    Shows how to raise and catch PlantError and WaterError
    individually, and demonstrates that catching GardenError
    catches all garden-related errors due to inheritance.
    """
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    garden_errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]
    for error in garden_errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")


if __name__ == "__main__":
    test_raising_errors()
