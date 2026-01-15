from .gateways import BooksGateway

# ============================================================
#                           BOOKS
# ============================================================
class BooksUsecase:
    def __init__(self):
        self.gateway = BooksGateway()

    def list_random_books(self, limit: int = 10):
        return self.gateway.get_random_books(limit=limit)

    def list_top_books(self, limit: int = 10):
        return self.gateway.get_top_books(limit=limit)