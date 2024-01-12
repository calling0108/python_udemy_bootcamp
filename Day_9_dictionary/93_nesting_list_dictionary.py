#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"], # key 하나에 한 개의 value만 가능하므로 list로 처리
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {
      "cities_visited": ["Paris", "Lille", "Dijon"], 
      "total_visits": 12
      },
  "Germany": {
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
      "total_visits": 5},
}

print(travel_log["France"]["cities_visited"])

#Nesting Dictionaries in Lists

travel_log_2 = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

print(f"printed is {travel_log_2[0]['cities_visited']}") # printed is ['Paris', 'Lille', 'Dijon']

print(travel_log_2[0]["country"]) # France
