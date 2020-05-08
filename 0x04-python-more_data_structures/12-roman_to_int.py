#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    rom = 0
    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for ch in range(len(roman_string)):
        if ch == len(roman_string) - 1:
            rom += nums[roman_string[ch]]
        elif nums[roman_string[ch]] >= nums[roman_string[ch + 1]]:
            rom += nums[roman_string[ch]]
        else:
            rom -= nums[roman_string[ch]]
    return rom
