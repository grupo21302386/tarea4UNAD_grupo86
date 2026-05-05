from cliente_reserva import Cliente, Reserva
from servicios import ServicioCorte, ServicioCejas, ServicioTinte
from utils import registrar_log

def ejecutar_operacion(numero, descripcion, funcion):
    print(f"\nOPERACIÓN {numero}: {descripcion}")

    try:
        resultado = funcion()
    except Exception as error:
        print(f"Error: {error}")
        registrar_log(error)
    else:
        print("Operación exitosa")
        if resultado:
            print(resultado)
    finally:
        print("Continuando ejecución...")

def main():

    ejecutar_operacion(
        1,
        "Cliente válido",
        lambda: Cliente("Jorge", "123456", "3001234567").mostrar_informacion()
    )

    ejecutar_operacion(
        2,
        "Cliente inválido",
        lambda: Cliente("", "123456", "3001234567").mostrar_informacion()
    )

    ejecutar_operacion(
        3,
        "Servicio corte",
        lambda: ServicioCorte("adulto").describir_servicio()
    )

    ejecutar_operacion(
        4,
        "Servicio inválido",
        lambda: ServicioCorte("viejo").describir_servicio()
    )

    print("\nSistema ejecutado correctamente")

if "name" == "_main_":
    main()