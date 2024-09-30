# dictionaries
# a dictionary  is acollection of many values
# dictionaries are a reprsentation of key values pairs

mycat = {"size": "fat", "color": "white"}

size_of_my_cat = mycat["size"]
color_of_my_cat = mycat["color"]

cars = {"brand": "lexus", "model": "IX-250"}

print("I have a" + cars["brand"] + " of " + " model " + cars["model"])

countries = {
    "france": "paris",
    "japan": "tokyo",
    "canada": "ottawa",
    "mongolia": "ulaanbaaataar",
}

capital_of_mongolia = countries["mongolia"]

school = {
    "class": "ss1"
}

numbers = {
    "number1":  1,
    "number2": 2, 
    "list1":  [0, 1, 2, 3, 4,],
    "dict1": {"one": 1, "two": 2}
    
}

animals = ["goat", "lion", "chimpazee", "gorrilla","python"]

python = animals[4]

print(size_of_my_cat, color_of_my_cat)
print(countries)

countries["nigeria"] = "abuja"
countries["USA"] = "washington Dc"
print(countries)


for key in list(countries.keys()):
    print("this a country")
    
for capital in list(countries.values()):
    print(capital)
for country, capital in countries.items():
    print("the capital of " + "country" +  " is " +  capital)