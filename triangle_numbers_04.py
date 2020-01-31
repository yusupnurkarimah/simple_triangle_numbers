string = ""
bar = 1

x = int(input("Please enter a number :"))
no = x
# Looping rows
while bar <= x: 

     # Looping empty spaces 
     kol = bar 
     while kol > 1:
          string = string + "   "
          kol = kol - 1
	
     # Looping right columns numbers
     kanan = 0
     while kanan <= (x - bar):
          string = string + " " + str(no) + " "
          kanan = kanan + 1	
		
     string = string + "\n"
     bar = bar + 1
     no = no - 1
print (string)