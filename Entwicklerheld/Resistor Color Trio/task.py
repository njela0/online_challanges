COLORS = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
]

def adjust_prefix(resistance):
    """Takes the resistance value as integer and returns a string with the resistance value and the adjusted prefix for the number of ohms"""
    resistance = str(resistance)
    prefix = ""

    if resistance.endswith("000000000"):
        prefix = "giga"
        resistance = resistance[:-9]

    elif resistance.endswith("000000"):
        prefix = "mega"
        resistance = resistance[:-6]

    elif resistance.endswith("000"):
        prefix = "kilo"
        resistance = resistance[:-3]

    return f"{resistance} {prefix}ohms"


def label(colors):
    """Takes a list of colors and calculates and returns the resistance in ohms as integer"""
    first_band = COLORS.index(colors[0])
    second_band = COLORS.index(colors[1])
    third_band = COLORS.index(colors[2])

    resistance = int(str(first_band) + str(second_band)) * (10 ** third_band)

    return adjust_prefix(resistance)


colors = ['blue', 'violet', 'white']
print(label(colors))
