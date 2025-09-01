#MadLib.py
#Name:Tavita
#Date:31 Aug 2025
#Assignment:MadLib

def main():
  print("Madlib")
  #Ask user for words
animal1 = input("Enter an animal:")
adj1 = input ("Enter an adjective:")
Ride1 = input ("Enter a choice of transportation: ")
NegE1 = input ("Enter negative emotion:")
Flavour1 = input("Enter ice cream flavour:")
place1 = input("Enter favorite place to go:")
Hab1 = input("Enter animal habitat:")

  #Print the story with the user supplied words.

print("Today I saw a ", animal1 + ".")
print("It was very", adj1 + ".")
print("I decided to show it the world in my", Ride1 + ".")
print("It was very", NegE1 + ", it said.")
print("I took", animal1+ "for some", Flavour1+ "ice cream to cheer it up" + ".")
print("We went to", place1+  "to watch the world unfold before us.")
print("I took it back home in the", Hab1 + ".")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
