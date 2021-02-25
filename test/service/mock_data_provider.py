class MockDataProvider:

    @staticmethod
    def get_mock_display():
        return [{"id": 1, "book_name": "hp", "author": 1, "category": 2, "count": 2},
                {"id": 2, "book_name": "david copperfield", "author": 2, "category": 1, "count": 3},
                {"id": 3, "book_name": "frankenstein", "author": 1, "category": 2, "count": 5}]

    @staticmethod
    def get_mock_aut():
        return [{"id": 1, "author_name": "Chetan", "aut_count": 1},
                {"id": 2, "author_name": "Mohan", "aut_count": 1}]

    @staticmethod
    def get_mock_cat():
        return [{"id": 1, "category_name": "Adventure", "cat_count": 1},
                {"id": 2, "category_name": "Thriller", "cat_count": 1}]

    count = 0
    @staticmethod
    def get_count():
        MockDataProvider.count += 1