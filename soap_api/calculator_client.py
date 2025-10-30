from zeep import Client, exceptions

class CalculatorClient:
    def __init__(self, wsdl_url: str = "http://www.dneonline.com/calculator.asmx?wsdl"):
        self.client = Client(wsdl_url)

    def add(self, a: int, b: int) -> int:
        return self.client.service.Add(a, b)

    def subtract(self, a: int, b: int) -> int:
        return self.client.service.Subtract(a, b)

    def multiply(self, a: int, b: int) -> int:
        return self.client.service.Multiply(a, b)

    def divide(self, a: int, b: int) -> float:
        try:
            return self.client.service.Divide(a, b)
        except exceptions.Fault as e:
            raise ValueError(f"SOAP Fault: {e}")
