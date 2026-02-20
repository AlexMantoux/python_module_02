class GardenError(Exception):
    """A basic error for garden problems."""
    pass


class PlantError(GardenError):
    """For problems with plants."""
    pass


class WaterError(GardenError):
    """For problems with watering."""
    pass


class GardenManager:
    """Manages a garden with plants, watering, and health checks."""

    def __init__(self) -> None:
        """Initialize the garden manager."""
        self.plants: dict = {}

    def add_plant(self, name: str) -> None:
        """Add a plant to the garden.

        Args:
            name: The name of the plant to add.

        Raises:
            PlantError: If the plant name is invalid.
        """
        if not name or not name.strip():
            raise PlantError("Plant name cannot be empty!")
        self.plants[name] = {"water": 0, "sun": 0}
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """Water all plants in the garden with cleanup."""
        print("Opening watering system")
        try:
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")
                self.plants[plant_name]["water"] = 5
        except Exception as e:
            print(f"Error during watering: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(
        self, name: str, water_level: int, sunlight_hours: int
    ) -> str:
        """Check the health of a plant.

        Args:
            name: The plant name.
            water_level: Water level between 1 and 10.
            sunlight_hours: Sunlight hours between 2 and 12.

        Returns:
            A health status message.

        Raises:
            PlantError: If the plant is not found.
            ValueError: If water_level or sunlight_hours are out of range.
        """
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found in garden!")
        if water_level < 1 or water_level > 10:
            if water_level > 10:
                raise ValueError(
                    f"Water level {water_level} is too high (max 10)"
                )
            raise ValueError(
                f"Water level {water_level} is too low (min 1)"
            )
        if sunlight_hours < 2 or sunlight_hours > 12:
            if sunlight_hours < 2:
                raise ValueError(
                    f"Sunlight hours {sunlight_hours} is too low (min 2)"
                )
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        self.plants[name]["water"] = water_level
        self.plants[name]["sun"] = sunlight_hours
        return f"{name}: healthy (water: {water_level}, sun: {sunlight_hours})"

    def water_error(self) -> None:
        """Simulate a water tank error.

        Raises:
            WaterError: Always raised to simulate empty tank.
        """
        raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    """Demonstrate all error handling techniques."""
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("\nAdding plants to garden...")
    for plant in ["tomato", "lettuce", ""]:
        try:
            manager.add_plant(plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    health_checks = [
        ("tomato", 5, 8),
        ("lettuce", 15, 6),
    ]
    for name, water, sun in health_checks:
        try:
            result = manager.check_health(name, water, sun)
            print(result)
        except (ValueError, PlantError) as e:
            print(f"Error checking {name}: {e}")

    print("\nTesting error recovery...")
    try:
        manager.water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
