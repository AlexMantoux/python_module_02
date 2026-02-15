class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_raising_errors():
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    try:
        print("Testing WaterError...")
        raise WaterError("Tomato")
    except WaterError as e:
        print(f"Caught PlantError: {e}")
    print()
    try:
        print("Testing catching all garden errors...")
        try:
            raise PlantError("The tomato plant is wilting!")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


test_raising_errors()
