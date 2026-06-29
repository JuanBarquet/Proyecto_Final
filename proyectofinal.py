import random

#DEFINIMOS LA CONDICION DEL GANADOR MEDIANTE UNA FUNCION
def ganador(usuario,computadora,reglas):
    if usuario == computadora:
        return "Empate"
    elif reglas[usuario] == computadora:
        return "Ganaste"
    else:
        return "Perdiste"

#EMPEZAMOS EL JUEGO
print("Bienvenido a Piedra, Papel o Tijera!")
opciones = ("piedra","papel","tijera")
reglas = {
    "piedra":"tijera",
    "papel":"piedra",
    "tijera":"papel",
}

#BUCLE PARA ESCOGER LA OPCION Y EVALUAR CONDICIONES
jugando = True
while jugando:
    usuario = input("Elige piedra, papel o tijera (o escribe 'salir' para terminar el juego):").lower()
    if usuario == "salir":
        jugando = False
        print("El juego ha terminado, gracias por participar")
        continue
    elif usuario not in opciones:
        print("Opcion invalida, escribe bien tu eleccion")
        continue

    #MEDIANTE LA FUNCION RANDOM Y METODO CHOICE ESCOGEMOS, LA COMPUTADORA ESCOGE UNA OPCION DE LA TUPLA
    computadora = random.choice(opciones)

    #SALIDA DE RESULTADOS
    print(f"Tu eleccion: {usuario}")
    print(f"Eleccion de Computadora: {computadora}")

    resultado = ganador(usuario,computadora,reglas)
    print(f"Resultado Final: {resultado}")