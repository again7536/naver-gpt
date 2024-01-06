from repository.concrete.naver_search_repository import NaverSearchRepository


class SearchRepository:
    search_repository = NaverSearchRepository()

    def __init__(self, impl=None):
        if impl is not None:
            self.search_repository = impl

    def search(self, query: str, section: str, limit=6):
        return self.search_repository.search(query, section, limit)
