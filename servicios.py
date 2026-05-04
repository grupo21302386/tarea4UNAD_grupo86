from abc import ABC, abstractmethod
from utils import DatoInvalidoError, ServicioNoDisponibleError

class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

class ServicioCorte(Servicio):
    precios = {
        "niño": 17000,
        "adolescente": 18000,
        "adulto": 20000
    }

    def _init_(self, categoria):
        super()._init_("Corte de cabello")
        self.categoria = categoria.lower().strip()
        self.validar_parametros()

    def validar_parametros(self):
        if self.categoria not in self.precios:
            raise ServicioNoDisponibleError("Categoría no válida")

    def calcular_costo(self, descuento=0, impuesto=0):
        return self.precios[self.categoria] - descuento + impuesto

    def describir_servicio(self):
        return f"{self.nombre} para {self.categoria}"

class ServicioCejas(Servicio):
    precios = {
        "sin tinte": 7000,
        "con tinte": 10000
    }

    def _init_(self, tipo):
        super()._init_("Diseño de cejas")
        self.tipo = tipo.lower().strip()
        self.validar_parametros()

    def validar_parametros(self):
        if self.tipo not in self.precios:
            raise ServicioNoDisponibleError("Tipo no válido")

    def calcular_costo(self, descuento=0, impuesto=0):
        return self.precios[self.tipo] - descuento + impuesto

    def describir_servicio(self):
        return f"{self.nombre} {self.tipo}"

class ServicioTinte(Servicio):
    def _init_(self):
        super()._init_("Corte con tinte")
        self.precio = 25000

    def validar_parametros(self):
        pass

    def calcular_costo(self, descuento=0, impuesto=0):
        return self.precio - descuento + impuesto

    def describir_servicio(self):
        return self.nombre


