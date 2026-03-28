def function1(text):
  return text + text

def function2(text):
  return text.title()

output = function2(function1("hello"))
print(output)
