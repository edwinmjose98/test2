import pytest
from BookManager.dataaccess.bookmanager_da import book_da



def test_insert_book1(db):
    res=book_da.insert_book("hp",1,1)
    assert res == 4
    # count=book_da.count()

def test_insert_book2(db):
    res = book_da.insert_book("hp", 1, 2)
    assert res == 1

def test_insert_author(db):
    res=book_da.insert_author("author2")
    assert res == 3

def test_insert_category(db):
    res = book_da.insert_category("test")
    assert res == 3

def test_get_author_id(db):
    author_id=book_da.get_author_id("Chetan")
    # print("hello")
    # print(author_id)
    assert author_id is not None
    assert author_id.id == 1

def test_get_category_id(db):
    category_id=book_da.get_category_id("Thriller")
    assert category_id is not None
    assert category_id.id == 2

def test_display(db):
    lis = book_da.display()
    assert len(lis) == 4

def test_display_aut(db):
    lis = book_da.display_authors()
    assert len(lis) >= 2

def test_display_cat(db):
    lis = book_da.display_categories()
    assert len(lis) == 3

def test_search_byauth(db):
    lis = book_da.search_byauth("Chetan")
    assert len(lis) == 3

def test_search_bycat(db):
    lis = book_da.search_bycat("Thriller")
    assert len(lis) == 2

def test_search_byname(db):
    lis=book_da.search_byname("hp")
    assert len(lis) == 2

def test_count(db):
    no = book_da.count("Thriller")
    assert no == 1

def test_update_book(db):
    book_da.update_book(3)
    lis = book_da.display()
    assert len(lis) == 2



def test_insert_customer(db):
    res=book_da.insert_customer("user3","user3")
    assert res == 1

def test_insert_admin(db):
    res=book_da.insert_admin("admin2","admin2")
    assert res == 2

# def test_display(db):
#     lis = BookDA.display()
#     assert len(lis) == 3
# def test_insert_book1(db):
#     res = BookDA.insert_book("testname", "testcat", "testaut")
#     assert res == 4
# def test_insert_book2(db):
#     res = BookDA.insert_book("hp", "Thriller", "Chetan")
#     assert res == 1
# def test_insert_author1(db):
#     res = BookDA.insert_author("test")
#     assert res == 4
# def test_insert_category1(db):
#     res = BookDA.insert_category("test")
#     assert res == 4
# def test_display_aut(db):
#     lis = BookDA.display_aut()
#     assert len(lis) >= 2
# def test_display_cat(db):
#     lis = BookDA.display_cat()
#     assert len(lis) == 4
# def test_search_aut(db):
#     lis = BookDA.search_aut("Chetan")
#     assert len(lis) == 2
# def test_search_cat(db):
#     lis = BookDA.search_cat("Thriller")
#     assert len(lis) == 2
# def test_count(db):
#     no = BookDA.count("Thriller")
#     assert no == 2
# def test_update_book(db):
#     BookDA.update_book(4)
#     lis = BookDA.display()
#     assert len(lis) == 3

if __name__ == '__main__':
    pytest.main()

