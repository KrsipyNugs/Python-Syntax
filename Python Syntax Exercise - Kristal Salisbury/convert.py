def convert_temp(unit_in, unit_out, temp):
    if unit_in != "f" and unit_in != "c":
        return f"Invalid unit {unit_in}"
    if unit_out != "f" and unit_out != "c":
        return f"Invalid unit {unit_out}"
    if unit_in == "f" and unit_out == "c":
        temp = (temp - 32) / 9 * 5
    if unit_in == "c" and unit_out == "f":
        temp = (temp * 5 / 9) + 32
    return temp    


print(convert_temp("c", "f", 0))
print(convert_temp("f", "c", 212))
print(convert_temp("z", "f", 32))
print(convert_temp("c", "z", 32))
print(convert_temp("f", "f", 75.5))

