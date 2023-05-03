
print('What do you want to grow?')
wish = input()

thisdict = {
  "Wheat": "January",
  "Chickpeas": "February",
  "Cumin": "March"
}

if wish in thisdict:
    print(f"Yes, {wish} is one a product I can grow for you")

else:
    print (f"I am afraid, {wish} is a product I cannot grow for you")

print('This is what I can grow for you')
x = thisdict.keys()
print (x)