def main(): 

     plate = input("Plate: ") 

     if is_valid(plate): 

         print("Valid") 

     else: 

         print("Invalid") 

  

  

 def is_valid(s): 

  

 # checking whether plate contains max of 6 chars and min of 2 chars, figure out why we used 'or' but not 'and' 

  

     if  len(s) < 2  or len(s) > 6 : 

         return False 

 # figure out why we used 'or' but not 'and' 

     if s[0].isalpha() == False or s[1].isalpha() == False: 

         return False 

  

 # nos. cannot be in the middle and must come at end and the first no. cannot be '0'. *here i is used to just initialse and terminate the while loop 

     i = 0 

     while i < len(s): 

           if s[i].isalpha() == False: 

              if s[i] == '0': 

                 return False 

              else: 

                 break 

           i += 1 

  

 # NO periods, puncuation marks and spaces are allowed 

  

     for c in s: 

         if c in ['.',' ','!','?']: 

            return False 

  

 # If we pass all the tests, return true 

     return True 

  

  

 main()
