def calculator():
    while(True):

      print("simple python calculator")
      try:
          a = int(input("number: "))
          x = int(input("number: "))
      except ValueError:
          print("can only use numbers")
          continue
      
      print("1.+ plus")
      print("2.- minus")
      print("3./ divide")
      print("4.* times")
      print("type 'quit' to stop")
      f = input()

      if f == "+" or "1":
          result = a + x

      if f == "-" or "2":
          result = a - x

      if f == "/" or "3":
          result = a / x
      
      if f == "*" or "4":
          result = a * x

      if f == "quit":
          break  

      print(result)
calculator()
    
