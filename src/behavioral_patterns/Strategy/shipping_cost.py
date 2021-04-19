class ShippingCost():

    def __init__(self, strategy):
        self._strategy = strategy

    
    ## calculate shipping cost
    def shipping_cost(self, order):
        return self._strategy.calculate(order)