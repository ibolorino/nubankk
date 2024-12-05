class Operation:
    orders: list
    taxes: list
    average_price: float
    quantity: int
    loss: float

    def __init__(self, orders):
        self.average_price = 0
        self.loss = 0
        self.quantity = 0
        self.orders = orders
        self.taxes = []
        for order in orders:
            self._process_order(order)

    def _process_order(self, order):
        order_result = (order.get("unit-cost") - self.average_price) * order.get("quantity")
        self._update_taxes(order, order_result)
        self._update_average_price(order)
        self._update_quantity(order)
        self._update_loss(order, order_result)
        

    def _update_average_price(self, order):
        if order.get("operation") == "buy":
            average_price = (self.average_price * self.quantity + order.get("unit-cost") * order.get("quantity"))/(self.quantity + order.get("quantity"))
            self.average_price = average_price

    def _update_quantity(self, order):
        if order.get("operation") == "buy":
            self.quantity += order.get("quantity")
        else:
            self.quantity -= order.get("quantity")

    def _update_loss(self, order, order_result):
        if order.get("operation") == "sell":
            self.loss += order_result
            if self.loss > 0:
                self.loss = 0

    def _update_taxes(self, order, order_result):
        total_value = order.get("unit-cost") * order.get("quantity")
        if order.get("operation") == "buy" or total_value <= 20000:
            tax = 0
        elif order_result <= 0:
            tax = 0
        elif order_result > abs(self.loss):
            tax = (order_result - abs(self.loss)) * 0.2
            tax = round(tax, 2)
        else:
            tax = 0
        self.taxes.append({"tax": tax})