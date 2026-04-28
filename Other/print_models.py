# fuction to import to other file

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


magicians = [
"Harry Houdini",
"David Copperfield",
"Penn Jillette",
"Teller",
"Derren Brown",
"Dynamo",
"Criss Angel",
"Ricky Jay",
"Doug Henning",
"Siegfried Fischbacher",
"Roy Horn",
"Shin Lim",
"Lance Burton",
"Juan Tamariz",
"Paul Daniels",
"Ali Bongo",
"The Amazing Kreskin",
"Mat Franco",
"Justin Willman",
"Piff the Magic Dragon"
]

def show_magicians():
    magicians = [
"Harry Houdini",
"David Copperfield",
"Penn Jillette",
"Teller",
"Derren Brown",
"Dynamo",
"Criss Angel",
"Ricky Jay",
"Doug Henning",
"Siegfried Fischbacher",
"Roy Horn",
"Shin Lim",
"Lance Burton",
"Juan Tamariz",
"Paul Daniels",
"Ali Bongo",
"The Amazing Kreskin",
"Mat Franco",
"Justin Willman",
"Piff the Magic Dragon"
]
    for magician in magicians:
        print(magician)

show_magicians()


# 8-9
def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def build_profile(first_name, last_name, age, city, country):
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    profile = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'city': city,
        'country': country
    }
    print("Profile created:")
    for key, value in profile.items():
        print(f"{key.capitalize()}: {value}")