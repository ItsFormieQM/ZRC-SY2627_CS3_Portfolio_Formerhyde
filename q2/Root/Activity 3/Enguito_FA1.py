class Publication():
    def __init__(self,title,author):
        self.__title = title
        self.__author = author
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def set_title(self, title):
        self.__title = title
    def set_author(self,author = "Unknown"):
        self.__author = author
    def display_info(self):
        print(f"{self.__class__.__name__} Information:")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        
class Book(Publication):
    def __init__(self,title,author,number_pages):
        super().__init__(title,author)
        self.__number_of_pages = number_pages
    def get_number_of_pages(self):
        print(f"Number of Pages: {self.__number_of_pages}")
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages <= -1:
            raise IndexError
        self.__number_of_pages = number_of_pages
class Magazine(Publication):
    def __init__(self,title,author,issue_number):
        super().__init__(title,author)
        self.__issue_number = issue_number
    def get_issue_number(self):
        print(f"Issue Number: {self.__issue_number}")
    def set_issue_number(self, issue_number):
        if issue_number <= -1:
            raise IndexError
        self.__issue_number = issue_number

t1 = Magazine("EXPERIENCE CHAPTER 1 GAME DEV LOGS LATEST","Formerhyde",0)
t1.set_issue_number(99)
t1.display_info()
t1.get_issue_number()
print("")
t1 = Book("EXPERIENCE CHAPTER 1 GAME DEV LOG HISTORY","Formerhyde",300)
t1.set_number_of_pages(99)
t1.display_info()
t1.get_number_of_pages()

t2 = Book("Documentation on how my type writer drawer works from the undertale/deltarune fangame name Experience (Chapter 1)", "Formerhyde",20)
t2.display_info()
t2.get_number_of_pages()