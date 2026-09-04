import random

country_gold_values = {
    "Afghanistan": 3, "Albania": 4, "Algeria": 3, "Andorra": 4, "Angola": 3,
    "Antigua_and_Barbuda": 4, "Argentina": 2, "Armenia": 3, "Australia": 1,
    "Austria": 2, "Azerbaijan": 3, "Bahamas": 3, "Bahrain": 3, "Bangladesh": 2,
    "Barbados": 3, "Belarus": 3, "Belgium": 2, "Belize": 4, "Benin": 4,
    "Bhutan": 4, "Bolivia": 3, "Bosnia_and_Herzegovina": 3, "Botswana": 4,
    "Brazil": 1, "Brunei": 4, "Bulgaria": 3, "Burkina_Faso": 4, "Burundi": 4,
    "Cabo_Verde": 4, "Cambodia": 3, "Cameroon": 3, "Canada": 1,
    "Central_African_Republic": 5, "Chad": 5, "Chile": 2, "China": 1,
    "Colombia": 2, "Comoros": 5, "Congo": 4, "Costa_Rica": 3,
    "Croatia": 3, "Cuba": 2, "Cyprus": 3, "Czechia": 2,
    "Democratic_Republic_of_the_Congo": 3, "Denmark": 2, "Djibouti": 5,
    "Dominica": 4, "Dominican_Republic": 3, "Ecuador": 3, "Egypt": 2,
    "El_Salvador": 3, "Equatorial_Guinea": 5, "Eritrea": 4, "Estonia": 3,
    "Eswatini": 4, "Ethiopia": 3, "Fiji": 4, "Finland": 2, "France": 1,
    "Gabon": 4, "Gambia": 4, "Georgia": 3, "Germany": 1, "Ghana": 3,
    "Greece": 2, "Grenada": 4, "Guatemala": 3, "Guinea": 4, "Guinea-Bissau": 5,
    "Guyana": 4, "Haiti": 3, "Honduras": 3, "Hungary": 2, "Iceland": 3,
    "India": 1, "Indonesia": 2, "Iran": 2, "Iraq": 2, "Ireland": 2,
    "Israel": 2, "Italy": 1, "Jamaica": 3, "Japan": 1, "Jordan": 3,
    "Kazakhstan": 3, "Kenya": 3, "Kiribati": 5, "Kuwait": 3, "Kyrgyzstan": 4,
    "Laos": 4, "Latvia": 3, "Lebanon": 3, "Lesotho": 5, "Liberia": 4,
    "Libya": 3, "Liechtenstein": 4, "Lithuania": 3, "Luxembourg": 3,
    "Madagascar": 4, "Malawi": 4, "Malaysia": 2, "Maldives": 4, "Mali": 4,
    "Malta": 3, "Marshall_Islands": 5, "Mauritania": 4, "Mauritius": 4,
    "Mexico": 1, "Micronesia": 5, "Moldova": 3, "Monaco": 3, "Mongolia": 3,
    "Montenegro": 4, "Morocco": 2, "Mozambique": 4, "Myanmar": 3, "Namibia": 4,
    "Nauru": 5, "Nepal": 3, "Netherlands": 1, "New_Zealand": 2, "Nicaragua": 3,
    "Niger": 5, "Nigeria": 2, "North_Korea": 2, "North_Macedonia": 3,
    "Norway": 2, "Oman": 3, "Pakistan": 2, "Palau": 5, "Panama": 3,
    "Papua_New_Guinea": 4, "Paraguay": 3, "Peru": 2, "Philippines": 2,
    "Poland": 2, "Portugal": 2, "Qatar": 3, "Romania": 2, "Russia": 1,
    "Rwanda": 4, "Saint_Kitts_and_Nevis": 5, "Saint_Lucia": 4,
    "Saint_Vincent_and_the_Grenadines": 5, "Samoa": 4, "San_Marino": 4,
    "Sao_Tome_and_Principe": 5, "Saudi_Arabia": 2, "Senegal": 3, "Serbia": 3,
    "Seychelles": 4, "Sierra_Leone": 4, "Singapore": 2, "Slovakia": 3,
    "Slovenia": 3, "Solomon_Islands": 5, "Somalia": 3, "South_Africa": 2,
    "South_Korea": 1, "South_Sudan": 3, "Spain": 1, "Sri_Lanka": 3,
    "Sudan": 3, "Suriname": 4, "Sweden": 2, "Switzerland": 1, "Syria": 2,
    "Tajikistan": 4, "Tanzania": 3, "Thailand": 2, "Timor-Leste": 4,
    "Togo": 4, "Tonga": 5, "Trinidad_and_Tobago": 3, "Tunisia": 3,
    "Turkey": 1, "Turkmenistan": 4, "Tuvalu": 5, "Uganda": 3, "Ukraine": 2,
    "United_Arab_Emirates": 2, "United_Kingdom": 1, "United_States": 1,
    "Uruguay": 3, "Uzbekistan": 3, "Vanuatu": 5, "Vatican_City": 4,
    "Venezuela": 2, "Vietnam": 2, "Yemen": 3, "Zambia": 4, "Zimbabwe": 3,
    "Taiwan": 2, "Kosovo": 4
}

player_name = input("Enter your name: ")
player_gold = 0
used_countries = set()
total_rounds = 30

# Group countries by starting letter
countries_by_letter = {}
for country in country_gold_values:
    first_letter = country[0].upper()
    if first_letter not in countries_by_letter:
        countries_by_letter[first_letter] = []
    countries_by_letter[first_letter].append(country)

print(f"\nWelcome {player_name}! Let's start the 30-question Study Quiz. The maximum points possible is 140. Not that you HAVE to capitalise every Name. Also every space is replaced by _")

for round_number in range(1, total_rounds + 1):
    available_letters = [letter for letter in countries_by_letter if len(countries_by_letter[letter]) > 0]

    if not available_letters:
        print("No more countries left!")
        break

    current_letter = random.choice(available_letters)

    print(f"\nQuestion {round_number}/{total_rounds}")
    print(f"Name a country starting with: {current_letter}")

    user_answer = input("> ")

    print( user_answer in country_gold_values)
    print( user_answer.startswith(current_letter))

    if (user_answer in country_gold_values and
        user_answer.startswith(current_letter)):



        if user_answer in used_countries:
            print(f" Already used '{user_answer}'!, no gold awarded!")
        else:
            gold_reward = country_gold_values[user_answer]
            player_gold += gold_reward
            used_countries.add(user_answer)
            countries_by_letter[current_letter].remove(user_answer)
            print(f" Correct! +{gold_reward} Gold.")
    else:
        print(" Incorrect.")

print("\n" + "="*30)
print(f"QUIZ COMPLETE, {player_name}!")
print(f"Total Gold: {player_gold}")
print(f"Countries Named: {len(used_countries)}")
print("="*30)


