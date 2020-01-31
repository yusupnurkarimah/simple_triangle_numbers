string = ""
bar = 1

x = int(input("Please enter a number :"))
no = 1
# Looping rows
while bar <= x: 
     # Looping columns 
     kol = bar 
     while kol > 0:
          string = string + " " + str(no) + " "
          kol = kol - 1

     string = string + "\n"
     bar = bar + 1
     no = no+1
print (string)