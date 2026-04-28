# 3-1

friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])

# 3-2

print(f"Hello, {friends[0]}!")
print(f"Hello, {friends[1]}!")
print(f"Hello, {friends[2]}!")
print(f"Hello, {friends[3]}!")
print(f"Hello, {friends[4]}!")

# 3-3

transportation = ["car", "bike", "bus", "train", "plane"]
print(f"I would like to own a {transportation[0]}.")
print(f"I would like to own a {transportation[1]}.")
print(f"I would like to own a {transportation[2]}.")
print(f"I would like to own a {transportation[3]}.")
print(f"I would like to own a {transportation[4]}.")

# 3-4

guests = ["Alice", "Bob", "Charlie", "David", "Eve"]
for guest in guests:
    print(f"Dear {guest}, you are invited to my dinner party!")


# 3-5

print(f"Sorry, {guests[2]}, I can't invite you to the dinner party.")
guests[2] = "Frank"
for guest in guests:
    print(f"Dear {guest}, you are invited to my dinner party!")

# 3-6

print("Good news! I found a bigger dinner table!")
guests.insert(0, "Grace")
guests.insert(2, "Heidi")
guests.append("Ivan")
for guest in guests:
    print(f"Dear {guest}, you are invited to my dinner party!")

# 3-7
print("Sorry, I can only invite two people for dinner.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to the dinner party.")
for guest in guests:
    print(f"Dear {guest}, you are still invited to my dinner party!")
del guests[0]
del guests[0]
print(guests)

# 3-8

destinations = ["Paris", "Tokyo", "New York", "Sydney", "Rome"]
print("Original list:")
print(destinations)
print("\nSorted list (temporary):")
print(sorted(destinations))
print("\nOriginal list after sorted():")
print(destinations)
print("\nSorted list (temporary, reverse):")
print(sorted(destinations, reverse=True))
print("\nOriginal list after sorted() with reverse:")
print(destinations)
print("\nReversed list (temporary):")
destinations.reverse()
print(destinations)
print("\nOriginal list after reverse():")
destinations.reverse()
print(destinations)
print("\nSorted list (permanent):")
destinations.sort()
print(destinations)
print("\nSorted list (permanent, reverse):")
destinations.sort(reverse=True)
print(destinations)

# 3-9

print(f"The number of guests invited to the dinner party is: {len(guests)}")

# 3-10(evrything in one file)

most_popular_languages = ["Python", "JavaScript", "Java", "C#", "C++"]
print("The most popular programming languages are:")
for language in most_popular_languages:
    print(language)

print("\nThe most popular programming languages in reverse order are:")
for language in reversed(most_popular_languages):
    print(language)

print("\nThe most popular programming languages sorted alphabetically are:")
for language in sorted(most_popular_languages):
    print(language)

print("\nThe most popular programming languages sorted in reverse alphabetical order are:")
for language in sorted(most_popular_languages, reverse=True):
    print(language)

print("\nThe original list of most popular programming languages is still unchanged:")
for language in most_popular_languages:
    print(language)

print("\nThe most popular programming languages sorted permanently in alphabetical order:")
most_popular_languages.sort()
for language in most_popular_languages:
    print(language)

print("\nThe most popular programming languages sorted permanently in reverse alphabetical order:")
most_popular_languages.sort(reverse=True)
for language in most_popular_languages:
    print(language)

print(f"\nThe number of most popular programming languages is: {len(most_popular_languages)}")

print("Done with lists!")