class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    plants: list[str] = []


    def add_plants(self, plant_name):
        self.plants.append(plant_name)

    def test_watering_system(self, plant_list: list[str]) -> None:
        print("Testing normal watering...")
        try:
            for plant in plant_list:
                print(f"Watering {plant}")
        except WaterError as e:
            print(f"Caught ValueError: {e}")
        finally:
            print("Closing watering system (cleanup)")
            print("Watering completed successfully!")

    def check_plant_health(
        self,
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


def test_garden_management():