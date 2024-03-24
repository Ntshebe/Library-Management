#Rewrite the entire task 1 and task 1B without using parameters and arguments in your functions

books = []
members = []

def add_Book():
    books.append({
        'book_Id': int(input("enter book id: ")),
          'title': input("enter title :"),
          'author': "Mthobisi",
          'status': "not Available"})

    """def add_Member(member_Id, name):
        members.append({
            'members_Id': input("Enter member Id"),
            'name': input("enter member name")
            'borrowed_books': []})"""
        
        
"""Task 1 A:
Suppose you use the system to add a book titled "Python Programming" written by Jacob Zuma with a 
book_id of 2024001, and a member named Anelisa Maleka with a member_id of 1. """
#call the function

add_Book()

#add_Member( "Anelisa Maleka",1)

#print statement
print("\n Book", books)
#print("\nMembers",members)