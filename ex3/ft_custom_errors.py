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


def main() -> None:
    print(PlantError("Test PlantError"))
    print(WaterError("Test WaterError"))
    print(GardenError("Test GardenError"))
    print(PlantError())
    print(WaterError())
    print(GardenError())


if __name__ == "__main__":
    main()
