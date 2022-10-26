import pandas as pd
import numpy as np

class BookLover():

    def __init__(self, name: str, email: str, fav_genre: str, num_books:int = 0, 
                 book_list = pd.DataFrame({'Book Name': pd.Series(dtype='str'), 
                                           'Book Rating': pd.Series(dtype='int')})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name:str, book_rating:int):
        new_book = pd.DataFrame({
            'Book Name': [book_name],
            'Book Rating': [book_rating]
        })
        if self.book_list['Book Name'].str.contains(book_name).any() == False:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            print("This title is already in the list")

    def has_read(self, book_name:str):
        if self.book_list['Book Name'].str.contains(book_name).any() == True:
            return True
        else:
            return False

    def num_books_read(self):
        return len(self.book_list)

    def fav_books(self):
        return self.book_list.loc[self.book_list['Book Rating'] > 3]
    
    
    
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    # And so forth
