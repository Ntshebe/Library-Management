books = []
members = []

def add_Book(book_Id, title, author, status):
    books.append({
        'book_Id': book_Id,
          'title': title,
          'author': author,
          'status': status})

def add_Member(member_Id, name):
        members.append({
            'members_Id': member_Id,
            'name': name,
            'borrowed_books': []})
        
        
"""Task 1 A:
Suppose you use the system to add a book titled "Python Programming" written by Jacob Zuma with a 
book_id of 2024001, and a member named Anelisa Maleka with a member_id of 1. """
#call the function

add_Book(2024001, "python Programming", "Jacob Zuma", "Available")

add_Member( "Anelisa Maleka",1)

#print statement
print("\n Book", books)
print("\nMembers",members)