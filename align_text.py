def align_text(t):
   i = 0
   counter = 0
   aligned_text = ""
   while(i < len(t)):
      aligned_text = aligned_text + t[i]
      i = i + 1
      counter = counter + 1
      if(counter == 30): #Change 30 to whatever lenght of characters each line should have!
         counter = 0
         aligned_text = aligned_text + "\n" 

   return aligned_text
      
txt = input("Give me text to align: ")
print(align_text(txt))

