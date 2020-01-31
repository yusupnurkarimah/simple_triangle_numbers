string = ""

x = int(input("Please enter a number :"))
bar = x
no = 0
# Looping rows
while bar >= 0:
	
     # Looping empty spaces
     kol = bar
     while kol > 0:
          string = string + "   "
          kol = kol - 1

     # Looping left columns numbers
     kiri = 1
     while kiri < (x - (bar-1)):
          string = string + " " + str(no) + " "
          kiri = kiri + 1		

     # Looping right columns numbers
     kanan = 1
     while kanan < kiri -1:
          string = string + " " + str(no) + " "
          kanan = kanan + 1	

     string = string + "\n\n"
     bar = bar - 1
     no = no + 1
print (string)