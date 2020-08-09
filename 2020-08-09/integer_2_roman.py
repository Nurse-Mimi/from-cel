class maths:
    def int_2_rom(self, num):
        value = [
            1000, 900, 500, 400,
            100, 90, 50, 40, 
            10, 9, 5, 4,
            1
            ]
        symbol = [
            "M", "CM", "D", "CD",
            "C", "KXC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        rom_num = ''
        i = 0
        while num > 0:
            for _ in range(num // value[i]):
                rom_num += symbol[i]
                num -= value[i]
            i += 1
        return rom_num

print(maths().int_2_rom(1))
print(maths().int_2_rom(1000))
print(maths().int_2_rom(300))
print(maths().int_2_rom(4000))
print(maths().int_2_rom(60))
print(maths().int_2_rom(5))
print(maths().int_2_rom(20000))
print(maths().int_2_rom(7))