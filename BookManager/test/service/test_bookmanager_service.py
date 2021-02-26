from matplotlib.figure import Figure

from BookManager.dataaccess.bookmanager_da import book_da
from BookManager.service.bookmanager_service import BookService
from BookManager.test.service.mock_data_provider import MockDataProvider
#
#
def test_display(mocker):
    mocker.patch.object(book_da, "display", return_value=MockDataProvider.get_mock_display())
    res = BookService.display()
    assert len(res) == 3

def test_display_auths(mocker):
    mocker.patch.object(book_da, "display_authors", return_value=MockDataProvider.get_mock_aut())
    res = BookService.display_auths()
    assert len(res) == 2

def test_display_cats(mocker):
    mocker.patch.object(book_da, "display_categories", return_value=MockDataProvider.get_mock_cat())
    res = BookService.display_cats()
    assert len(res) == 2
#
def test_insert(mocker):
    mocker.patch.object(book_da, "insert_author", return_value=3)
    mocker.patch.object(book_da, "insert_category", return_value=3)
    mocker.patch.object(book_da, "get_author_id", return_value=1)
    mocker.patch.object(book_da, "get_category_id", return_value=2)
    res = BookService.insert("testname", "testcat", "testaut")
    assert res == 5

def test_display_byauth(mocker):
    mocker.patch.object(book_da, "search_byauth", return_value="success")
    res = BookService.display_byauth("test")
    assert res == "success"
# #
def test_display_bycat(mocker):
    mocker.patch.object(book_da, "search_bycat", return_value="success")
    res = BookService.display_bycat("test")
    assert res == "success"
# #
def test_buy(mocker):
    mocker.patch.object(book_da, "update_book", return_value=MockDataProvider.get_count())
    BookService.buy([1])
    i = MockDataProvider.count
    assert i == 1

def test_create_figure1(mocker):
    mocker.patch.object(book_da, "count", return_value=1)
    mocker.patch.object(book_da, "display_categories", return_value=MockDataProvider.get_mock_cat())
    res = BookService.create_figure1()
    assert type(res) == Figure