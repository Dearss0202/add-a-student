#Her ses vores imports.
import os
import winsound
import time

#Her definere vi hvad der står i vores menu.
def display_menu():
    os.system('cls')
    os.system('color 0A')
    print("Program opret bruger v1")
    print("---Hovedmenu--- \n")
    print("H: Hjælp")
    print("T: Tilmeld elev")
    print("V: hvis tilmeldte elever")
    print("S: slet alt data")
    print("A: Afslut program \n")

#Her definere vi hvad der står i vores Hjælp.
def display_help(): 
    os.system('cls')
    print("-- Vis hjælp -- \n")
    print("H: Hjælp \n hvis denne hjælp \n")
    print("T: Tilmeld elev \n Her oprettes en elev med navn og adresse \n")
    print("V: Vis tilmeldte elever \n Her vises alle elever i systemet \n")
    print("S: Slet alle data \n Alle data slettes! \n Du skal svare J til du ønsker at slette data \n")
    print("A: Afslut program \n Programmet afsluttes \n")
    input("Tryk enter for at fortsætte")
    os.system('cls')

winsound.Beep(frequency=37, duration=10)
display_menu()

#Her definere vi hvad der står og sker når vi tilmelder en elev.
def display_tilmeld():
  os.system('cls')
  print("-- Tilmeld elever -- \n")
  navn = input("Tast elevens navn --> ")
  adresse = input("Tast elevens adresse --> ")
  if os.path.exists("Elever.txt"):
        mode = "a"  
  else:
        mode = "x"  
        
  with open("Elever.txt", mode) as f:
        f.write(navn + " " + adresse + "\n")
  print()
  input("Tryk enter for at fortsætte")
  os.system('cls')
  
  display_menu()
  
#Her definere vi hvad der står i vores tilmeldte elever.
def display_elever():
  os.system('cls')
  print("-- Vis tilmeldte elever -- \n")
  if os.path.exists("Elever.txt"):
    f = open("Elever.txt", "r" )
    print(f.read())
  else:
    print("Der er ingen elever på listen endnu.")  
    
  print()
  input("Tryk enter for at fortsætte")
  os.system('cls')
  display_menu()

  
#Her definere vi hvad der står og sker når vi sletter vores elever.txt file.
def display_slet():
  os.system('cls')
  print("-- Slet alt data -- \n")
  if os.path.exists("Elever.txt"):
    print("Du kan ikke fortryde sletning \n")
    time.sleep(3)
    choice = input("Er du sikker på du vil slette J/N  --> ")
  
    if choice == 'J':
      os.remove("Elever.txt")
      input("Tryk enter for at fortsætte")
      display_menu()
  
    elif choice == 'N':
      input("Tryk enter for at fortsætte")
      os.system('cls')
      display_menu()
      
  else:
    print("Der er ikke nogle elevlister så der er ikke noget at slette.")
    
  input("Tryk enter for at fortsætte")
  os.system('cls')
  display_menu()
    
    

#vores program kører i den her loop til A er trykket.    
while True:
    choice = input("Tast valg og enter -> ")
    
    if choice == 'H':
        display_help()
        display_menu()
        
    elif choice == 'T':
      display_tilmeld()
      
    elif choice == 'V':
      display_elever()   
      
    elif choice == 'S':
      display_slet() 
      
    elif choice == 'A':
      exit()