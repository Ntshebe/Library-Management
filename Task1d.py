#Rewrite the entire Task 1 C using Data frames instead of lists.

import pandas as pd 



books = []
members = []


BOOKD= ({
        'book_Id': [int(input("enter book id: "))],
          'title': [input("enter title :")],
          'author': ["Mthobisi"],
          'status': ["not Available"]})

dfBooks = pd.DataFrame(BOOKD)
print("Data frame of books", dfBooks)

MEMBERD= ({
            'members_Id': [input("Enter member Id: ")],
            'name': [input("enter member name: ")],
            'borrowed_books': [[]]})
pdMembers= pd.DataFrame(MEMBERD)
            
            

        
  

#add_Member( "Anelisa Maleka",1)

#print statement
print("\n Book", books)
print("\nMembers",members)