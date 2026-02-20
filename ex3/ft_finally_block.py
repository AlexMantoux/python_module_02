class WaterError(Exception):
    """Error raised when a watering operation fails."""
    pass


def test_watering_system(plant_list: list[str]) -> None:
    """Test the watering system with a list of plants.

    Opens the watering system, attempts to water each plant,
    and always closes the system in a finally block even if
    an error occurs.

    Args:
        plant_list: A list of plant names to water. If a plant
                    is None, a WaterError is raised.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise WaterError("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    finally:
        print("Closing watering system (cleanup)")
        print("Watering completed successfully!")


def water_plants(plant_list: list[str]) -> None:
    """Water all plants in the given list using the watering system.

    Args:
        plant_list: A list of plant names to water.
    """
    print("=== Garden Watering System ===")
    print()
    test_watering_system(plant_list)


if __name__ == "__main__":
    plant_list1: list[str] = ["tomato", "lettuce", "carrots"]
    plant_list2: list[str] = ["tomato", None, "carrots"]
    print("Testing normal watering...")
    water_plants(plant_list1)
    print("Testing with error...")
    water_plants(plant_list2)
    print()
    print("Cleanup always happens, even with errors!")
