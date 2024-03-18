from abc import ABC, abstractmethod

class kendaraan(ABC):
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class mobil(kendaraan):
    def __init__(self, merek, model, tahun):
        super().__init__(merek, model, tahun)
        self.running = False
    def start(self):
        if not self.running:
            print(f"{self.merek} {self.model} engine started.")
            self.running = True
        else:
            print(f"{self.merek} {self.model} engine is already running.")
    def stop(self):
        if self.running:
            print(f"{self.merek} {self.model} engine stopped.")
            self.running = False
        else:
            print(f"{self.merek} {self.model} engine is already stopped.")

class Motor(kendaraan):
    def __init__(self, merek, model, tahun):
        super().__init__(merek, model, tahun)
        self.running = False
    def start(self):
        if not self.running:
            print(f"{self.merek} {self.model} engine started.")
            self.running = True
        else:
            print(f"{self.merek} {self.model} engine is already running.")
    def stop(self):
        if self.running:
            print(f"{self.merek} {self.model} engine stopped.")
            self.running = False
        else:
            print(f"{self.merek} {self.model} engine is already stopped.")

mobil1 = mobil("Toyota", "Corolla", 2020)
motor1 = Motor("Honda", "CBR1000R", 2021)
for i in (mobil1,motor1):
    i.start()
    i.start()
    i.stop()
    i.stop()
    print()


