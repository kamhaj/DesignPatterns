''' 
provide a family of algorithms, encapsulate each one 
and make them interchangable

since it a family of algorithms, they will operate with the same 
set of inputs and outputs (pass common object as input)
'''

""" 
Example: Shipping calculator (calculate shipping costs)

We support different shippers:
    Postal Service
    UPS
    Federal Express

It must be extensible (possible new shippers on the market)
"""

from shipping_cost import ShippingCost
from strategy.order import Order
from strategy.fedex_strategy import FedExStrategy 
from strategy.postal_strategy import PostalStrategy
from strategy.ups_strategy import UPSStrategy

# Test Federal Express shipping

# there is depencency inversion problem here (direct call to Order), but there is another pattern to fix it - factory pattern
order = Order()                 # before it was Order(Shipper), Single Responsibility rule violation
strategy  = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

# Test UPS shipping

order = Order()
strategy  = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

# Test Postal Service shipping

order = Order()
strategy  = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0


print("\nTests passed.\n")