string = ""
bar = 1

x = int(input("Please enter a number :"))
print ("\n")
no = x
# Looping rows
while bar < x: 

     # Looping empty spaces 
     kol = bar 
     while kol > 1:
          string = string + "   "
          kol = kol - 1

     # Looping left columns numbers
     kiri = 0
     while kiri <= (x - bar): 
          string = string + " " + str(no) + " " 
          kiri = kiri + 1 

     # Looping right columns numbers 
     kanan = kiri 
     while kanan > 1:
          string = string + " " + str(no) + " "
          kanan = kanan - 1

     if (bar+1) <= x: 
          string = string + "\n\n" 
          bar = bar + 1 
no = no -1 # Looping rows 
bar = x-1 
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