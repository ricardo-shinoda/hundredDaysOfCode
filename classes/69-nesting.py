capitals = {
    "Brazil": "Brasilia",
    "Canada": "Otawa",
}

# Nested List in Dictionary

travel_log = {
    "Brazil": ["São Paulo", "Campinas", "Guarulhos"],
    "Canada": ["Toronto", "Quebec", "Montreal"],
}

# printing Campinas
print(travel_log["Brazil"][1])


nested_list = ["A", "B", ["c", "d"]]
# printing letter "d"
print(nested_list[2][0])


travel_statistic = {
    "Brazil": ["São Paulo", "Campinas", "Guarulhos"],
    "Canada": {
        "num_times_visited": 8,
        "cities_visited": ["Toronto", "Quebec", "Montreal"],
    },
}

# printing Quebec
print(travel_statistic["Canada"]["cities_visited"][1])
