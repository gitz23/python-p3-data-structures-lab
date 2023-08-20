spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
   return [food_name["name"] for food_name in spicy_foods]
#print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return [food_name for food_name in spicy_foods if food_name["heat_level"] > 5]
#print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food_name for food_name in spicy_foods if food_name["cuisine"] == cuisine]
#print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

# spicy_food ={
#         'name': 'Griot',
#         'cuisine': 'Haitian',
#         'heat_level': 10,
# }
# def create_spicy_food(spicy_foods, spicy_food):
#     return spicy_foods.append(spicy_food)
# print(spicy_foods,spicy_food)