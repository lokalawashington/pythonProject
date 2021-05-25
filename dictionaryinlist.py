travel_log = [
    {
        "country": "france",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 12,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_visited, time_visited, city_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = time_visited
    new_country["cities"] = city_visited
    travel_log.append(new_country)


add_new_country("russia", 2, ["moscow", "saint petersburg"])
print(travel_log)
