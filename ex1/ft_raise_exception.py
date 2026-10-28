#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp in range(0, 41):
        return (temp)
    else:
        raise ValueError("Temperature bad for plants(min 0°C, max 40°C)")


def test_temperature() -> None:
    test: list[str] = ['25', 'abc', '100', '-50']
    for i in test:
        try:
            inp = input_temperature(i)
            print(inp)
        except Exception as e:
            print(e)


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
