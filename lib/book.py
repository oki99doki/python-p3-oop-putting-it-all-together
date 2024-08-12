#!/usr/bin/env python3


#       '''prints "page_count must be an integer" if page_count is not an integer.'''
#       book = Book("And Then There Were None", 272)
#       captured_out = io.StringIO()
#       sys.stdout = captured_out
#       book.page_count = "not an integer"
#       sys.stdout = sys.__stdout__
#       assert captured_out.getvalue() == "page_count must be an integer\n"


import ipdb
class Book:
    #pass
    def __init__(self, title, page_count):
        
        
        self.title = title
        self.page_count = page_count
        #self.page_count = page_count

        #if isinstance(page_count, int):
        #    self.page_count = page_count
        #else:
            #raise AssertionError("{page_count} must be an integer")
        #    print("page_count must be an integer\n")

        '''
        if isinstance(self.page_count, int):
            pass
        else:
            print("page_count must be an integer\n")
        '''



    @property
    def page_count(self):
          return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
           print("page_count must be an integer")




    #page_count = 0

    '''
    def count_pages(self, page_count):
        if isinstance(page_count, int):
            self.page_count = page_count
        else:
            #self.page_count = "not an integer"
            raise AssertionError("page_count must be an integer\n")
    '''
            
    def turn_page(self):
        #self.page_count = self.page_count + 1
        print("Flipping the page...wow, you read fast!")



##sample = Book("Nomen est Omen", 234)
#print(sample)

##sample.title
#print(sample.title)

##sample.page_count
#print(sample.page_count)

##sample.count_pages(sample)
#print(sample.count_pages(sample))
#ipdb.set_trace()

#ipdb.set_trace()