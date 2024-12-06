from services import Operation
import json
import sys


def main() -> None:
    operations = [line.strip() for line in sys.stdin.readlines()]
    operations = [json.loads(operation) for operation in operations if operation != '']
    
    for orders in operations:
        op = Operation(orders)
        print(op.taxes)
    return


if __name__ == "__main__":
    main()
