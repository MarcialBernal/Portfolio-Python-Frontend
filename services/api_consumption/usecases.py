from .gateways import ApiConsumptionGateway

# ============================================================
#                           BOOKS
# ============================================================
class RawgGenresUsecase:
    def __init__(self):
        self.gateway = ApiConsumptionGateway()

    def list_genres(self):
        return self.gateway.get_rawg_genres()