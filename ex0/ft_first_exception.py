#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    test: list[str] = ['25', 'abc']
    for i in test:
        try:
            inp = input_temperature(i)
        except Exception as e:
            print(e)
            return
        print(inp)


test_temperature()
