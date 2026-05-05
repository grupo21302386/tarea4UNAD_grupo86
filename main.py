from cliente_reserva import Cliente, Reserva
from servicios import ServicioCorte

def main():
    print("Sistema completo funcionando")

    # Crear cliente
    cliente = Cliente("Jorge", "123456", "3001234567")

    # Crear servicio
    servicio = ServicioCorte("adulto")

    # Crear reserva
    reserva = Reserva(cliente, servicio, 30)
    reserva.confirmar()

    # Mostrar resultado
    print(reserva.mostrar_reserva())

if __name__ == "__main__":
    main()