class Package:
    def __init__(self, id, sender, recipient, address):
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.address = address
        self.status = "Pending"

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

class Delivery:
    def __init__(self, courier, package):
        self.courier = courier
        self.package = package
        self.status = "Pending"

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

class Courier:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.deliveries = []

    def add_delivery(self, delivery):
        self.deliveries.append(delivery)

    def get_deliveries(self):
        return self.deliveries

class DeliverySystem:
    def __init__(self):
        self.packages = []
        self.couriers = []

    def add_package(self, package):
        self.packages.append(package)

    def add_courier(self, courier):
        self.couriers.append(courier)

    def get_packages(self):
        return self.packages

    def get_couriers(self):
        return self.couriers

    def assign_delivery(self, courier, package):
        delivery = Delivery(courier, package)
        courier.add_delivery(delivery)
        package.set_status("In Transit")
        delivery.set_status("In Transit")

    def complete_delivery(self, delivery):
        delivery.set_status("Delivered")
        delivery.package.set_status("Delivered")