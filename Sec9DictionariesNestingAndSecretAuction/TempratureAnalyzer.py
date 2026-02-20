city_temperatures = {
    "Karachi": 36,
    "Lahore": 28,
    "Islamabad": 22,
    "Quetta": 15,
    "Murree": 8
}
for temperature in city_temperatures:
  weather = city_temperatures[temperature]
  if weather > 35:
    city_temperatures[temperature] = "Very Hot"
  elif weather > 25:
    city_temperatures[temperature] = "warm"
  elif weather > 15:
    city_temperatures[temperature] = "cool"
  else:
    city_temperatures[temperature] = "very cold"

print(city_temperatures)
