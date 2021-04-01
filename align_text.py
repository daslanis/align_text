"""
NOTE: align_text_with_underscore() Is not the best option...
"""

def align_text_with_underscore(t):
   i = 0
   counter = 0
   aligned_text = ""
   while(i < len(t)):
      aligned_text = aligned_text + t[i]
      i = i + 1
      counter = counter + 1
      if(counter == 30): #Change 30 to whatever lenght of characters each line should have!
         counter = 0
         if(t[i]!=" "):
            aligned_text = aligned_text + "_\n" 
         else:
            aligned_text = aligned_text + "\n" 
            
   return aligned_text

def align_text_without_underscore(t):
   i = 0
   counter = 0
   aligned_text = ""

   while(i < len(t)):
      if(counter < 30):
         aligned_text = aligned_text + t[i]
      elif(t[i] == " "):
         aligned_text = aligned_text + "\n"
         counter = -1
      else:
         aligned_text = aligned_text + t[i]
         
      i = i + 1
      counter = counter + 1
      
   return aligned_text

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(align_text_with_underscore(txt))
print("\n-------------------------------\n")
print(align_text_without_underscore(txt))
