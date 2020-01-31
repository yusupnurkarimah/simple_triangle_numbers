string = ""

bar = int(input("Please enter a number :"))
no = bar
# Looping rows
while bar >= 0:

     # Looping columns
     kol = bar
     while kol > 0:
          string = string + " " + str(no) + " "
          kol = kol - 1
		
     string = string + "\n"
     bar = bar - 1
     no = no - 1
print (string)