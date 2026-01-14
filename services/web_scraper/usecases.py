from services.web_scraper.gateways import ScraperGateway

class ScraperUsecase:
    def __init__(self):
        self.gateway = ScraperGateway()

    def search_items(self, query: str):
        return self.gateway.search_items(query)