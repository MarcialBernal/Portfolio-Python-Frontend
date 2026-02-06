from .gateways import AutoMLGateway

# ============================================================
#                   AUTO ML
# ============================================================

class AutoMLPredictionUsecase:
    def __init__(self):
        self.gateway = AutoMLGateway()

    def get_prediction(self):
        return self.gateway.get_prediction()
