capital = {
    "Francis": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    # nesting  dictionary
    # "Francis": {"city_visied":["Paris", "Lille", "Dijon"], "total_visits": 12 },
    "Francis": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
# ["A", "B",["C", "D",]] NESTING LIST
print(travel_log)
