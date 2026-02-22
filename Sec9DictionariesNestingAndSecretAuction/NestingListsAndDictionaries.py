capitals = {
"France":"Paris",
"Germany": "Berlin"
}

# nested list in dictionary

travel_log = {
  "France":["Paris","Lille", "Dijon"],
  "Germany":["Stutgratt","Berlin"]
}
# to print lille we will
print(travel_log["France"][1])

nested_list = ["A","B",["C","D"]]
# to print d
print(nested_list[2][1])

travel_log = {
  "France" : {
    "cities_visited":["paris", "Dijon", "Lille"],
    "total_visits": 5
},
  "Germany": {
    "cities_visited":["Berlin", "Stutgratt", "Humburg"],
    "total_visits":5

  }

}
print(travel_log["Germany"])
