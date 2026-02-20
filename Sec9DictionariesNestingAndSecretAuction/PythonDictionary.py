programing_dictionaries = {
"Bug":"An Error in program which prevents program from running as expected",
"Function": "A piece of code which can be called again and again if needed",
"Loop":"The Action of doing something over and over again"
}
print(programing_dictionaries["Bug"])

# This is how we add another key in the dictiory as a programming way

programing_dictionaries["Comment"] = "A block or line of code which is not executed in output"
print(programing_dictionaries)

# emptying a dictionary
# programing_dictionaries = {}
# print(programing_dictionaries)

# Editing a key in dictionary
programing_dictionaries["Bug"] = "A bug is a moth in your dictionary if you didnt fix it it will burn it self"
print(programing_dictionaries)

# Loop through
for Keys in programing_dictionaries:
  print(Keys)
  print(programing_dictionaries[Keys])
