from abc import ABC, abstractmethod


class Entidad(ABC):
    @abstractmethod
    def mostrar_informacion(self):
        pass


class Cliente(Entidad):
    def __init__(self, nombre, documento, telefono):
        self.__nombre = self.validar_nombre(nombre)
        self.__documento = self.validar_documento(documento)
        self.__telefono = self.validar_telefono(telefono)

    def validar_nombre(self, nombre):
        if not nombre or nombre.strip() == "":
            raise DatoInvalidoError("El nombre del cliente no puede estar vacío.")
        return nombre.strip()

    def validar_documento(self, documento):
        if not str(documento).isdigit():
            raise DatoInvalidoError("El documento debe contener solo números.")
        return str(documento)

    def validar_telefono(self, telefono):
        if not str(telefono).isdigit():
            raise DatoInvalidoError("El teléfono debe contener solo números.")
        return str(telefono)

    def obtener_nombre(self):
        return self.__nombre

    def mostrar_informacion(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Teléfono: {self.__telefono}"
        )


class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.validar_reserva()

    def validar_reserva(self):
        if not isinstance(self.cliente, Cliente):
            raise ReservaInvalidaError("La reserva debe tener un cliente válido.")

        if not isinstance(self.servicio, Servicio):
            raise ReservaInvalidaError("La reserva debe tener un servicio válido.")

        if not isinstance(self.duracion, int) or self.duracion <= 0:
            raise ReservaInvalidaError("La duración debe ser un número entero mayor que cero.")

    def confirmar(self):
        if self.estado == "Cancelada":
            raise ReservaInvalidaError("No se puede confirmar una reserva cancelada.")

        self.estado = "Confirmada"
        registrar_log(f"Reserva confirmada para {self.cliente.obtener_nombre()}.")

    def cancelar(self):
        if self.estado == "Cancelada":
            raise ReservaInvalidaError("La reserva ya se encuentra cancelada.")

        self.estado = "Cancelada"
        registrar_log(f"Reserva cancelada para {self.cliente.obtener_nombre()}.")

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo()

        except Exception as error:
            registrar_log(f"Error al procesar reserva: {error}")
            raise ReservaInvalidaError("No se pudo procesar la reserva.") from error

        else:
            self.estado = "Procesada"
            registrar_log(f"Reserva procesada correctamente. Valor: ${costo}")
            return costo

        finally:
            registrar_log("Finalizó el intento de procesamiento de reserva.")

    def mostrar_reserva(self):
        return (
            f"Cliente: {self.cliente.obtener_nombre()} | "
            f"Servicio: {self.servicio.describir_servicio()} | "
            f"Duración: {self.duracion} minutos | "
            f"Estado: {self.estado}"
        )