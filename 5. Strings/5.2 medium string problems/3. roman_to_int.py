def romanToInt(s):
    transistion = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    s.replace('IV', 'IIII')
    s.replace('IX', 'VIIII')
    s.replace('XL', 'XXXX')
    s.replace('XC', 'LXXXX')
    s.replace('CD', 'CCCC')
    s.replace('CM', 'DCCCC')
    
    count = 0

    for each in s:
        count += transistion[each]

    return count


print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("IX"))
print(romanToInt("IV"))
print(romanToInt("III"))    
print(romanToInt("LVIII"))
