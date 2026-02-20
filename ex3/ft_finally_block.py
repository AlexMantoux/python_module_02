class WaterError(Exception):
    pass


def test_watering_system(plant_list: list[str]) -> None:
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


def water_plants(plant_list) -> None:
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
