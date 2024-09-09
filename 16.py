# Try Except

try:
    print(t)
except:
    print("Error Occured")



try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")



try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")



try:
  print(Z)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")



try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")





try:
    Age = int(input("Enter your Age: "))

    if Age >= 18 and Age <= 60:
        print("You are eligible for voting")
    elif Age > 60:
        print("You are old citizen you can vote from home")
    elif Age < 18:
        print("You are not eligible for voting")
    else:
        print("You Ruinned the Program")
    
except:
    print("Out of Box")