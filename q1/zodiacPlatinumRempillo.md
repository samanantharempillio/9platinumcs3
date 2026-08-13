birth_year = int(input("Enter your birth year: "))
zodiac_signs = [
"Rat (鼠 / Shǔ)"
, "Ox (牛 / Niú)"
, "Tiger (虎 / Hǔ)"
, "Rabbit (兔 / Tù)"
, "Dragon (龙 / Lóng)"
, "Snake (蛇 / Shé)"
, "Horse (马 / Mǎ)"
, "Goat (羊 / Yáng)"
, "Monkey (猴 / Hóu)"
, "Rooster (鸡 / Jī)"
, "Dog (狗 / Gǒu)"
, "Pig (猪 / Zhū)"
]


if birth_year >= 1900:
    birth_year = birth_year
else:
    print("Invalid year, should  be more than 1900")


remainder = birth_year % 12


print("Your Chinese Zodiac Sign is: ",zodiac_signs[remainder-4])
