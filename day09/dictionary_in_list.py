travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

def add_new_country(name, times_visited, cities_visited):
    new_country = {}

    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited

    travel_log.append(new_country)


country = input("Enter country name: ")
visits = int(input("Enter number of visits: "))
cities = input("Enter cities separated by comma: ").split(",")

# Remove extra spaces from city names
for i in range(len(cities)):
    cities[i] = cities[i].strip()

add_new_country(country, visits, cities)

print(f"\nI've been to {travel_log[-1]['country']} {travel_log[-1]['visits']} times.")
print(f"My favourite city was {travel_log[-1]['cities'][0]}.")