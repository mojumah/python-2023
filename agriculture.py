
print('What do you want to grow?')
wish = input()


thisdict = {
  "Wheat": "January",
  "Chickpeas": "February",
  "Cumin": "March"
}

month = thisdict[wish]

if wish in thisdict:
    print(f"Yes, {wish} is one a product I can grow for you")
    print(f"You have to grow {wish} in {month}")

else:
    print (f"I am afraid, {wish} is a product I cannot grow for you") 

print('This is what I can grow for you')
capability = thisdict.keys()
print (capability)