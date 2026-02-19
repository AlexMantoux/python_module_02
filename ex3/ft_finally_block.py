class WateringError(Exception):
    pass


def test_watering_system(plant_list: list[str]) -> None:
    print("Testing normal watering...")
    try:
        for plant in plant_list:
            print(f"Watering {plant}")
    except WateringError as e:
        print(f"Caught ValueError: {e}")
    finally:
        print("Closing watering system (cleanup)")
        print("Watering completed successfully!")

    print()
    print("Testing with error...")
    try:
        for plant in plant_list:
            print(f"Watering {plant}")
            raise WateringError("Error: Cannot water None - invalid plant!")
    except WateringError as e:
        print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")
        print()
        print("Cleanup always happens, even with errors!")


def water_plants(plant_list) -> None:
    test_watering_system(plant_list)


def main() -> None:
    plant_list = ["tomato", "lettuce", "carrots"]
    print("=== Garden Watering System ===")
    print()
    water_plants(plant_list)
