class GardenError(Exception):
    pass

class PlantError(Exception):
    pass

class WaterError(Exception):
    pass



def test_raising_errors():
    print("=== Custom Garden Errors Demo ===")