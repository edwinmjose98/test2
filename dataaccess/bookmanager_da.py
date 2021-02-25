from BookManager.model.book import Book
from BookManager.model.author import Author
from BookManager.model.category import Category
from BookManager.model.user import User

class book_da:

    @classmethod
    def insert_book(cls, name: str, author_id , category_id):
        # author = Author.select().where(Author.id == author_id).get()
        # print(type(author))
        # category = Category.select().where(Category.id == category_id).get()
        query = Book.select().where((Book.name == name) & (Book.category_id == category_id) & (Book.author_id == author_id))
        # print(author_id)
        # print(category_id)
        # print(query)
        # print(query.exists())
        if query.exists():
            # print(" in ")
            q=query.get()
            query2=Book.update(count = Book.count + 1).where(q.id == Book.id)
            return query2.execute()
        else:
            query= Book.insert(name=name, author_id=author_id, category_id=category_id)
            return query.execute()


    @classmethod
    def insert_author(cls, name: str):
        try:
            reply= Author.select().where(Author.author_name==name).get()
            return reply
        except:
            query = Author.insert(author_name=name)
            return query.execute()

    @classmethod
    def insert_category(cls,name:str):
        reply = Category.select().where(Category.category_name == name)
        if reply.exists():
            q = reply.get()
            query2 = Category.update(cat_count=Category.cat_count + 1).where(q.category_name == Category.category_name)
            # print(query2)
            return query2.execute()
        else:
            query = Category.insert(category_name=name)
            return query.execute()

        # try:
        #     reply= Category.select().where(Category.category_name==name).get()
        #     return reply
        # except:
        #     query = Category.insert(category_name=name)
        #     return query.execute()

    @classmethod
    def get_author_id(cls,name:str):
        query=Author.select(Author.id).where(Author.author_name==name).first()
        return query

    @classmethod
    def get_category_id(cls, name: str):
        query = Category.select(Category.id).where(Category.category_name == name).first()
        return query

    @classmethod
    def display(cls):
        query = Book.select(Book.id, Book.name, Category.category_name, Author.author_name)\
            .join(Author, on=(Book.author_id == Author.id))\
            .join(Category, on=(Book.category_id == Category.id))
        return list(query.dicts())

    @classmethod
    def display_authors(cls):
        query=Author.select()
        return list(query.dicts())

    @classmethod
    def display_categories(cls):
        query = Category.select()
        return list(query.dicts())

    @classmethod
    def search_byauth(cls, name: str):
        try:
            author = Author.select().where(Author.author_name == name).get()
            query = Book.select(Book.id, Book.name, Category.category_name, Author.author_name)\
                .join(Category).join(Author, on=(Book.author_id == Author.id)).where(Book.author_id == author)
            # list(book_da.search_bycat(name).dicts())
            return list(query.dicts())
        except:
            return -1

    @classmethod
    def search_bycat(cls, name: str):
        try:
            category = Category.select().where(Category.category_name == name).get()
            # print(type(category))
            query = Book.select(Book.id, Book.name, Category.category_name, Author.author_name) \
                .join(Author).join(Category, on=(Book.category_id == Category.id)).where(Book.category == category)
            return list(query.dicts())
        except:
            return -1

    @classmethod
    def search_byname(cls, name:str):
        try:
            query = Book.select(Book.id, Book.name, Category.category_name, Author.author_name) \
                .join(Author, on=(Book.author_id == Author.id)).join(Category, on=(Book.category_id == Category.id)).where(Book.name == name)
            return list(query.dicts())
        except:
            return -1

    @classmethod
    def update_book(cls, id:int):
        check = Book.select().where(Book.id == id).get()
        c = Category.select().where(Category.id == check.category_id).get()
        if check.count > 1:
            query = Book.update(count=Book.count - 1).where(id == Book.id)
        else:
            query = Book.delete().where(Book.id == id)
        query.execute()
        if c.cat_count > 1:
            query = Category.update(cat_count=Category.cat_count - 1).where(c.category_name == Category.category_name)
        else:
            query = Category.delete().where(c.category_name == Category.category_name)
        query.execute()


        # query=Books.delete().where(Books.id==id)
        # return query.execute()

    @classmethod
    def count(cls, name: str):

        c = Category.select().where(Category.category_name == name).get()
        return c.cat_count


        # c = Books.select(Books.id, Books.name, Category.category_name, Author.author_name) \
        #     .join(Author, on=(Books.author_id == Author.id)) \
        #     .join(Category, on=(Books.category_id == Category.id)).where(Category.category_name == name).count()
        # return c

    @classmethod
    def insert_customer(cls,username,password):
        q=User.select().where(User.username==username)
        if q.exists():
            return -1
        else:
            query = User.insert(username=username, password=username, Role="Customer")
            return query.execute()
    @classmethod
    def insert_admin(cls, username, password):
        q = User.select().where(User.username == username)
        if q.exists():
            return -1
        else:
            query = User.insert(username=username, password=username, Role="Admin")
            return query.execute()

    @classmethod
    def get_user(cls,username):
        user = User.select().where(User.username == username).get()
        return user

    @classmethod
    def get_password(cls, username):
        password=User.select(User.password).where(User.username == username).get()
        return password.password

    @classmethod
    def check_username(cls, username):
        try:
            q = User.select().where(User.username == username).get()
            return 1
        except:
            return -1

# print(len(list(book_da.display_categories().dicts())))

# book_da.insert_book("abc","1","2")
# print(list(book_da.search_bycat("adventure").dicts()))