from services import Operation
import json


def main():
    operations = []
    operation = input()
    print("##################")
    print(operation)
    print("##################")
    while operation:
        operations.append(json.loads(operation))
        operation = input()
    for orders in operations:
        op = Operation(orders)
        print(op.taxes)
    return


if __name__ == "__main__":
    main()

