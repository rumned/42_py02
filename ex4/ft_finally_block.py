#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, error_msg: str = "Unknown garden error"):
        super().__init__(error_msg)


class PlantError(GardenError):
    def __init__(self, error_msg: str = "Unknown plant error"):
        super().__init__(error_msg)


class WaterError(GardenError):
    def __init__(self, error_msg: str = "Unknown water error"):
        super().__init__(error_msg)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"{plant_name} capitalized, watering success")
    else:
        raise PlantError(f"Invalid plant name: \'{plant_name}\'")


def test_watering_system() -> None:
    print("==Open watering system==")
    plants = ["Tomato", "Pomelo", "Banana", "banana", "apple"]
    try:
        for p in plants:
            water_plant(p)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        return
    finally:
        print("Ending tests, return to main")
        print("==Close watering system==\n")
        print("Cleanup always happens even with errors")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
