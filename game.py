from random import randint 
import os
game = 1
while(game):
  os.system('clear')
  trynum = 3
  print("Tahmin et hangi kelime:\n")
  a = ["test", "se", "ben", "deneme", "adam"]
  ans = randint(0,4)
  string = a[ans]
  while(trynum):
    if(trynum == -1):
      print("Canların bitti.")
      print("Bir daha oyna?\n[E/H]: ")
      inr = input()
      if(inr == "E"):
        game = 1
        trynum = 3
      elif(inr == "H"):
        game = 0
    print("Kalan can",trynum)
    inp = input("Kelime:")
    if(inp != string):
      print("Hatalı kelime")
      if(trynum == 1):
        trynum = -1
      else:
        trynum = trynum-1
    elif(inp == string):
      print("Doğru kelime!\n")
      print("Bir daha oyna?\n[E/H]: ")
      inr = input()
      if(inr == "E"):
        game = 1
        trynum = 3
      elif(inr == "H"):
        game = 0
        
  




