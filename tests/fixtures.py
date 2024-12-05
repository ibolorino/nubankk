def set_case_tests_as_dict():
    case_tests = (
        (
            [
                {"operation":"buy", "unit-cost":10.00, "quantity": 100},
                {"operation":"sell", "unit-cost":15.00, "quantity": 50},
                {"operation":"sell", "unit-cost":15.00, "quantity": 50}
            ], 
            [
                {"tax": 0.00},{"tax": 0.00},{"tax": 0.00}
            ]
        ),
        (
            [
                {"operation":"buy", "unit-cost":10.00, "quantity": 10000},
                {"operation":"sell", "unit-cost":20.00, "quantity": 5000},
                {"operation":"sell", "unit-cost":5.00, "quantity": 5000}
            ],
            [
                {"tax": 0.00},{"tax": 10000.00},{"tax": 0.00}
            ]
        ),
        (
            [
                {"operation":"buy", "unit-cost":10.00, "quantity": 10000},
                {"operation":"sell", "unit-cost":5.00, "quantity": 5000},
                {"operation":"sell", "unit-cost":20.00, "quantity": 3000}
            ],
            [
                {"tax": 0.00},{"tax": 0.00},{"tax": 1000.00}
            ]
        ),
        (
            [
                {"operation":"buy", "unit-cost":10.00, "quantity": 10000},
                {"operation":"buy", "unit-cost":25.00, "quantity": 5000},
                {"operation":"sell", "unit-cost":15.00, "quantity": 10000}
            ],
            [
                {"tax": 0.00},{"tax": 0.00},{"tax": 0.00}
            ]
        ),
        (
            [
                {"operation":"buy", "unit-cost":10.00, "quantity": 10000},
                {"operation":"buy", "unit-cost":25.00, "quantity": 5000},
                {"operation":"sell", "unit-cost":15.00, "quantity": 10000},
                {"operation":"sell", "unit-cost":25.00, "quantity": 5000}
            ],
            [
                {"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 10000.00}
            ]
        ),
        (
            [
                {"operation":"buy", "unit-cost":10.00, "quantity": 10000},
                {"operation":"sell", "unit-cost":2.00, "quantity": 5000},
                {"operation":"sell", "unit-cost":20.00, "quantity": 2000},
                {"operation":"sell", "unit-cost":20.00, "quantity": 2000},
                {"operation":"sell", "unit-cost":25.00, "quantity": 1000}
            ],
            [
                {"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 3000.00}
            ]
        ),
        (
            [
                {"operation":"buy", "unit-cost":10.00, "quantity": 10000},
                {"operation":"sell", "unit-cost":2.00, "quantity": 5000},
                {"operation":"sell", "unit-cost":20.00, "quantity": 2000},
                {"operation":"sell", "unit-cost":20.00, "quantity": 2000},
                {"operation":"sell", "unit-cost":25.00, "quantity": 1000},
                {"operation":"buy", "unit-cost":20.00, "quantity": 10000},
                {"operation":"sell", "unit-cost":15.00, "quantity": 5000},
                {"operation":"sell", "unit-cost":30.00, "quantity": 4350},
                {"operation":"sell", "unit-cost":30.00, "quantity": 650}
            ],
                [
                   {"tax":0.00}, {"tax":0.00}, {"tax":0.00}, {"tax":0.00}, {"tax":3000.00}, {"tax":0.00}, {"tax":0.00}, {"tax":3700.00}, {"tax":0.00}
                ] 
        ),
        (
            [
                {"operation":"buy", "unit-cost":10.00, "quantity": 10000},
                {"operation":"sell", "unit-cost":50.00, "quantity": 10000},
                {"operation":"buy", "unit-cost":20.00, "quantity": 10000},
                {"operation":"sell", "unit-cost":50.00, "quantity": 10000}
            ],
            [
                {"tax":0.00},{"tax":80000.00},{"tax":0.00},{"tax":60000.00}
            ]
        )
    )
    return case_tests

def set_case_tests_as_str():
    case_tests = (
        (
            '[{"operation":"buy", "unit-cost":10.00, "quantity": 100},{"operation":"sell", "unit-cost":15.00, "quantity": 50},{"operation":"sell", "unit-cost":15.00, "quantity": 50}]', 
            "[{'tax': 0}, {'tax': 0}, {'tax': 0}]\n"
        ),
        # (
        #     '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":20.00, "quantity": 5000},{"operation":"sell", "unit-cost":5.00, "quantity": 5000}]',
        #     "[{'tax': 0}, {'tax': 10000.0}, {'tax': 0}]\n"
        # ),
        # (
        #     '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":5.00, "quantity": 5000},{"operation":"sell", "unit-cost":20.00, "quantity": 3000}]',
        #     "[{'tax': 0}, {'tax': 0}, {'tax': 1000.0}]\n"
        # ),
        # (
        #     '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"buy", "unit-cost":25.00, "quantity": 5000},{"operation":"sell", "unit-cost":15.00, "quantity": 10000}]',
        #     "[{'tax': 0}, {'tax': 0}, {'tax': 0}]\n"
        # ),
        # (
        #     '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"buy", "unit-cost":25.00, "quantity": 5000},{"operation":"sell", "unit-cost":15.00, "quantity": 10000},{"operation":"sell", "unit-cost":25.00, "quantity": 5000}]',
        #     "[{'tax': 0}, {'tax': 0}, {'tax': 0}, {'tax': 10000.0}]\n"
        # ),
        # (
        #     '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":2.00, "quantity": 5000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":25.00, "quantity": 1000}]',
        #     "[{'tax': 0}, {'tax': 0}, {'tax': 0}, {'tax': 0}, {'tax': 3000.0}]\n"
        # ),
        # (
        #     '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":2.00, "quantity": 5000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":25.00, "quantity": 1000},{"operation":"buy", "unit-cost":20.00, "quantity": 10000},{"operation":"sell", "unit-cost":15.00, "quantity": 5000},{"operation":"sell", "unit-cost":30.00, "quantity": 4350},{"operation":"sell", "unit-cost":30.00, "quantity": 650}]',
        #     "[{'tax': 0}, {'tax': 0}, {'tax': 0}, {'tax': 0}, {'tax': 3000.0}, {'tax': 0}, {'tax': 0}, {'tax': 3700.0}, {'tax': 0}]\n"
        # ),
        # (
        #     '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":50.00, "quantity": 10000},{"operation":"buy", "unit-cost":20.00, "quantity": 10000},{"operation":"sell", "unit-cost":50.00, "quantity": 10000}]',
        #     "[{'tax': 0}, {'tax': 80000.0}, {'tax': 0}, {'tax': 60000.0}]\n"
        # )
    )
    return case_tests