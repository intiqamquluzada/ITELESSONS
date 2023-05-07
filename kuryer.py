class Sifaris:
    def __init__(self, id, gonderen, alici, address):
        self.id = id
        self.gonderen = gonderen
        self.alici = alici
        self.address = address
        self.status = "Davam eden"

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status


class Catdirilma:
    def __init__(self, kuryer, sifaris):
        self.kuryer = kuryer
        self.sifaris = sifaris
        self.status = "Davam eden"

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status


class Kuryer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.deliveries = []

    def add_delivery(self, delivery):
        self.deliveries.append(delivery)

    def get_deliveries(self):
        return self.deliveries


class CatdirilmaSistemi:
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
        delivery = Catdirilma(courier, package)
        courier.add_delivery(delivery)
        package.set_status("Yolda")
        delivery.set_status("Yolda")

    def complete_delivery(self, delivery):
        delivery.set_status("Catdirildi")
        delivery.package.set_status("Catdirildi")

print(555)
