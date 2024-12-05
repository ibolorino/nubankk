import unittest
from services import Operation
from fixtures import set_case_tests_as_dict


class TestOperation(unittest.TestCase):
    def setUp(self):
        self.operation = Operation(orders=[])

    def test_update_average_price_buy(self):
        self.operation.average_price = 20
        self.operation.quantity = 100
        order = {"operation": "buy", "unit-cost": 10.00, "quantity": 100}
        self.operation._update_average_price(order)
        self.assertEqual(self.operation.average_price, 15)

    def test_update_average_price_sell(self):
        self.operation.average_price = 5
        order = {"operation": "sell", "unit-cost": 10.00, "quantity": 100}
        self.operation._update_average_price(order)
        self.assertEqual(self.operation.average_price, 5)

    def test_update_quantity_buy(self):
        self.operation.quantity = 100
        order = {"operation": "buy", "unit-cost": 10.00, "quantity": 100}
        self.operation._update_quantity(order)
        self.assertEqual(self.operation.quantity, 200)

    def test_update_quantity_sell(self):
        self.operation.quantity = 100
        order = {"operation": "sell", "unit-cost": 10.00, "quantity": 100}
        self.operation._update_quantity(order)
        self.assertEqual(self.operation.quantity, 0)

    def test_update_loss_buy(self):
        self.operation.average_price = 10
        self.operation.quantity = 100
        self.operation.loss = -500
        order = {"operation": "buy", "unit-cost": 10.00, "quantity": 100}
        order_result = (order.get("unit-cost") - self.operation.average_price) * order.get("quantity")
        self.operation._update_loss(order, order_result)
        self.assertEqual(self.operation.loss, -500)

    def test_update_loss_sell(self):
        self.operation.average_price = 10
        self.operation.quantity = 100
        self.operation.loss = -500
        order = {"operation": "sell", "unit-cost": 5, "quantity": 100}
        order_result = (order.get("unit-cost") - self.operation.average_price) * order.get("quantity")
        self.operation._update_loss(order, order_result)
        self.assertEqual(self.operation.loss, -1000)

    def test_update_taxes_buy(self):
        order = {"operation": "buy", "unit-cost": 10.00, "quantity": 100}
        order_result = 1000
        self.operation._update_taxes(order, order_result)
        self.assertEqual(self.operation.taxes[-1], {"tax": 0})

    def test_update_taxes_total_lower_20000(self):
        order = {"operation": "sell", "unit-cost": 10.00, "quantity": 100}
        order_result = 1000
        self.operation._update_taxes(order, order_result)
        self.assertEqual(self.operation.taxes[-1], {"tax": 0})

    def test_update_taxes_result_lower_0(self):
        order = {"operation": "sell", "unit-cost": 50.00, "quantity": 1000}
        order_result = -1000
        self.operation._update_taxes(order, order_result)
        self.assertEqual(self.operation.taxes[-1], {"tax": 0})

    def test_update_taxes_result_lower_loss(self):
        self.operation.loss = -2000
        order = {"operation": "sell", "unit-cost": 50.00, "quantity": 1000}
        order_result = 1000
        self.operation._update_taxes(order, order_result)
        self.assertEqual(self.operation.taxes[-1], {"tax": 0})

    def test_update_taxes_result_greater_loss(self):
        self.operation.loss = -2000
        order = {"operation": "sell", "unit-cost": 50.00, "quantity": 1000}
        order_result = 3000
        self.operation._update_taxes(order, order_result)
        self.assertEqual(self.operation.taxes[-1], {"tax": 200})
        
    def test_process_order(self):
        case_tests = set_case_tests_as_dict()
        for input_parameter, expected_value in case_tests:
            op = Operation(orders=[])
            for order in input_parameter:
                op._process_order(order)
            self.assertEqual(op.taxes, expected_value)
            