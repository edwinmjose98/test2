from matplotlib.figure import Figure

from BookManager.dataaccess.bookmanager_da import book_da


class BookService:
    @classmethod
    def display(cls):
        return book_da.display()

    @classmethod
    def display_cats(cls):
        return book_da.display_categories()


    @classmethod
    def display_auths(cls):
        return book_da.display_authors()

    @classmethod
    def insert(cls, name: str, aut: str, cat: str):
        r1=book_da.insert_author(aut)
        r2=book_da.insert_category(cat)
        result=book_da.insert_book(name, book_da.get_author_id(aut), book_da.get_category_id(cat))
        return result

    @classmethod
    def insert_customer(cls, name, password):
        result=book_da.insert_customer(username=name, password=password)
        return result

    @classmethod
    def insert_admin(cls, name, password):
        result = book_da.insert_admin(username=name, password=password)
        return result


    @classmethod
    def display_bycat(cls, name: str):
        return book_da.search_bycat(name)

    @classmethod
    def display_byauth(cls, name: str):
        return book_da.search_byauth(name)

    @classmethod
    def display_byname(cls, name:str):
        return book_da.search_byname(name)

    @classmethod
    def buy(cls, lis):
        for b in lis:
            book_da.update_book(b)

    @classmethod
    def get_user(cls, username):
        user = book_da.get_user(username=username)
        return user

    @classmethod
    def get_password(cls, username):
        password=book_da.get_password(username=username)
        return password


    @classmethod
    def create_figure1(cls):
        label = []
        sizes = []
        list = BookService.display_cats()
        for b in list:
            label.append(b['category_name'])
            sizes.append(book_da.count(b['category_name']))

        fig = Figure()
        axis = fig.add_subplot()
        axis.pie(sizes, labels=label, autopct='%1.1f%%', shadow=True, startangle=90)
        axis.axis('equal')
        return fig

    @classmethod
    def check_username(cls, username):
        res=book_da.check_username(username=username)
        return res
        # try:
        #     q = User.select().where(User.username == username).get()
        #     return 1
        # except:
        #     return -1

# print(BookService.display_cats())

