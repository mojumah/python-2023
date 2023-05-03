
print('What do you want to grow?')
wish = input()

thisdict = {
  "Wheat": "January",
  "Chickpeas": "February",
  "Cumin": "March"
}

if wish in thisdict:
    print(f"Yes, {wish} is one of the keys in this dictionary")

print('This is what I can grow for you')
x = thisdict.keys()
print (x)