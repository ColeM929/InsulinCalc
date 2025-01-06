import math


def add(x, y):
  return x + y


def subtract(x, y):
  return x - y


def multiply(x, y):
  return x * y


def divide(x, y):
  return x / y

userinput = input("Welcome! Use command 'help' to see commands\n")
if userinput == "help":
  print("Commands:")
  print("help: Prints this help message")
  print("start: Starts the program")
  print("frecipes: Show (Mostly) carb-free recipes")
elif userinput == "start":
  targetbg = float(input("What is the target blood glucose? "))
  correctionfactor = float(input("What is the correction factor? "))
  itocarb = float(input("What is the insulin to carb ratio? "))
  currentbg = float(input("What is the current blood glucose? "))
  abovetarget = float(subtract(currentbg, targetbg))
  insulintocorrectbg = float(divide(abovetarget, correctionfactor))
  sumofcarb = float(input("What is the sum of the carbs? "))
  insulintocovercarb = float(divide(sumofcarb, itocarb))
  tcid = float(add(insulintocorrectbg, insulintocovercarb))
  rounded_tcid = round(tcid * 2) / 2  
  print(rounded_tcid)
elif userinput == "frecipes":
  print("Carb free recipes")
  print("1: Cheese stick: 1 carb")
  print("2: Beef Jerky: 6 carbs")
  print("3: Dum-Dum pop: 5 carbs")
  print("4: Smartfood: 9 carbs")
  print("More soon!")
