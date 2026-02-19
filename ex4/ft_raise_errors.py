def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
        ) -> None:
    if (plant_name == ""):
        raise TypeError("Error: Plant name cannot be empty!")
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
                         "is too hight (max 12)")


def test_plant_checks() -> None:
    plant_name: str = "tomato"
    water_level: int = 7
    sunlight_hours: int = 8

    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    try:
        check_plant_health(plant_name, water_level, sunlight_hours)
        print(f"Plant '{plant_name}' is healthy!")
    except (TypeError, ValueError) as e:
        print(f"{e}")
    print()
    print("Testing empty plant name...")
    try:
        plant_name = ""
        check_plant_health(plant_name, water_level, sunlight_hours)
        print(f"Plant '{plant_name}' is healthy!")
    except (TypeError, ValueError) as e:
        print(f"{e}")
    print()
    print("Testing bad water level...")
    try:
        plant_name: str = "tomato"
        water_level: int = 15
        sunlight_hours: int = 8
        check_plant_health(plant_name, water_level, sunlight_hours)
        print(f"Plant '{plant_name}' is healthy!")
    except (TypeError, ValueError) as e:
        print(f"{e}")
    print()
    print("Testing bad sunlight hours...")
    try:
        water_level: int = 7
        sunlight_hours: int = 0
        check_plant_health(plant_name, water_level, sunlight_hours)
        print(f"Plant '{plant_name}' is healthy!")
    except (TypeError, ValueError) as e:
        print(f"{e}")
    print()
    print("All error raising tests completed!")
