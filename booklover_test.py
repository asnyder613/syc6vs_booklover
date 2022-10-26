import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    
    
    def test_1_add_book(self):
        book1 = BookLover('Sarah', 'noemail@gmail.com', 'sci-fi')
        book1.add_book('Jane Eyre', 4)

        #expected to be in book_list
        self.assertTrue('Jane Eyre' in book1.book_list['Book Name'].to_list(), "FAILURE: the book was not added")
    
    
    def test_2_add_book(self):
        book1 = BookLover('Sarah', 'noemail@gmail.com', 'sci-fi')
        book1.add_book('The Divine Comedy', 5)
        book1.add_book('The Divine Comedy', 5)

        #expected to be in book_list only once
        self.assertTrue(book1.book_list['Book Name'].to_list().count('The Divine Comedy')==1, "FAILURE: this item is in the list more than once")
        
        
    def test_3_has_read(self):
        book1 = BookLover('Sarah', 'noemail@gmail.com', 'sci-fi')
       
        # add books
        book1.add_book('Fight Club', 3)
        book1.add_book('The Divine Comedy', 5)
        book1.add_book('The Popol Vuh', 5)

        #expected response True
        expected = True
        self.assertEqual(book1.has_read('Fight Club'), expected, "FAILURE: the book was not found")
        
        
    def test_4_has_read(self):
        book1 = BookLover('Sarah', 'noemail@gmail.com', 'sci-fi')
        # add books
        book1.add_book('Fight Club', 3)
        book1.add_book('The Divine Comedy', 5)
        book1.add_book('The Popol Vuh', 5)

        # test has_read
        self.assertFalse(book1.has_read("The Tempest"), "FAILURE: the book should not exist in the list")
        
        
    def test_5_num_books_read(self):
        book1 = BookLover('Sarah', 'noemail@gmail.com', 'sci-fi')
        # add books
        book1.add_book('Fight Club', 3)
        book1.add_book('The Divine Comedy', 5)
        book1.add_book('The Popol Vuh', 5)

        # test num_books_read
        #expected is 3
        expected = 3
        self.assertEqual(book1.num_books_read(), expected, "FAILURE: there should be 3 books in the list")
        
        
    def test_6_fav_books(self):
        book1 = BookLover('Sarah', 'noemail@gmail.com', 'sci-fi')
        # add books
        book1.add_book('Fight Club', 3)
        book1.add_book('The Divine Comedy', 1)
        book1.add_book('The Popol Vuh', 5)

        #test fav_books
        #expected to be in favorite book_list
        self.assertTrue('The Popol Vuh' in book1.book_list['Book Name'].to_list(), "FAILURE: the book was not found in favorite books list")
    
        
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)