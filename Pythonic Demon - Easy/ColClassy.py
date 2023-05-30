#Simple Color Classifier

def classify(color):
    red, green, blue = color

    if red > 200 and green < 50 and blue < 50:
        return "Red"
    elif red < 50 and green < 50 and blue > 200:
        return "Blue"
    elif red < 50 and green > 200 and blue < 50:
        return "Green"
    elif red > 200 and green > 200 and blue < 50:
        return "Yellow"
    elif red > 200 and green < 50 and blue > 200:
        return "Purple"
    elif red < 50 and blue > 200 and green > 200:
        return "Cyan"
    elif red == blue == green == 255:
        return "White" 
    else:
        return "Unknown"

colors = [(255,0,0),(0,255,0),(0,0,255),(225,208,35),
          (245,10,222),(255,255,255),(150, 150, 150)]

for x in colors:
    category = classify(x)
    print(f"The color {x} belongs to the category: {category}")
