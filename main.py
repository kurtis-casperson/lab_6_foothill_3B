# Challenge 1

# The code below assigns the 5th letter of each word in food to the new list fifth. 
# However, the code currently produces errors. Insert a try/except clause that will allow 
# the code to run and produce of list of the 5th letter in each word. If the word is not long enough, 
# it should not print anything out. Note: The pass statement is a null operation; nothing will happen when it executes.





food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

def fifth_letter(fifth, food):

   
    for x in food:
        try:
         fifth.append(x[4])
         
        except IndexError as string_too_short:
            string_too_short
        continue
    print(fifth)  


fifth_letter(fifth, food)



