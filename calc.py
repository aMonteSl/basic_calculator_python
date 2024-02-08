#!/usr/bin/python3

from sys import argv
import operaciones as op

SUMA = "suma"
RESTA = "resta"
EJEMPLO_ARGUMENTOS = "Ejemplo: python3 suma 1 4"
ERROR_ARGUMENTO_OPERACION = "No has indicado que operación(suma/resta) quieres realizar en los argumentos"
ERROR_ARGUMENTO_NUMERO = "Los argumentos que hacen referencia a los números no estan de la forma correcta"
ERROR_INPUT_OPERACION = "Input incorrecto, ponga una operación valida (suma/resta)"
ERROR_INPUT_NUMERO = "Input incorrecto, ponga número"
ERROR_GENERAL = "No has lanzado el programa de forma correcta, hay dos modos (argumentos/inputs)"
EXPLICACION_MODO_ARGUMENTOS = "Si desea lanzar por modo argumentos aquí tiene un ejemplo."
EXPLICACION_MODO_INPUTS = ("Si desea lanzar por modo inputs únicamente lanze el programa sin argumentos."
                           " Ejemplo python3 calc.py")
PEDIR_OPERACION = "-Que operación quieres hacer: "
PEDIR_NUM1 = "-Dame el primer número: "
PEDIR_NUM2 = "-Dame el segundo número: "
MODO_ARGUMENTOS = "Has introducido argumentos, la calculadora hará los calculos con los argumentos"
MODO_INPUTS = "No has introducido argumentos, por lo tanto te voy a pedir que operacion quieres hacer y los números"


def pedir_numeros():
    exit1, exit2 = False, False
    number1, number2 = None, None
    while not exit1:
        try:
            number1 = int(input(PEDIR_NUM1))
            exit1 = True
        except ValueError:
            print(ERROR_INPUT_NUMERO)
    while not exit2:
        try:
            number2 = int(input(PEDIR_NUM2))
            exit2 = True
        except ValueError:
            print(ERROR_INPUT_NUMERO)

    return number1, number2


def pedir_operacion():
    finish = False
    operacion_mat = None
    while not finish:
        operacion_mat = input(PEDIR_OPERACION).lower()
        if operacion_mat == SUMA or operacion_mat == RESTA:
            finish = True
        else:
            print(ERROR_INPUT_OPERACION)

    return operacion_mat


def manejo_argumentos(argumentos):
    # Manejo de losargumentos pasados por el usuario, pasar a int los números y ver la operación
    operacion_mat = argumentos[1].lower()
    try:
        number1 = int(argumentos[2])
        number2 = int(argumentos[3])
    except ValueError:
        # En caso de error con los argumentos que suponemos que son números informamos al usuario de su error
        print(ERROR_ARGUMENTO_NUMERO + ". " + EJEMPLO_ARGUMENTOS)
        # Este exit() evita que el programa continue después del error con los argumentos, evitando futuros errores
        exit()

    return operacion_mat, number1, number2


def manejo_inputs():
    # Pedir la operacion que se va a querer realizar
    operacion_mat = pedir_operacion()

    # Pedir los numeros a sumar o restar, aqui esta el control de ValueError
    number1, number2 = pedir_numeros()

    return operacion_mat, number1, number2


def seleccionar_operacion(operacion_mat, number1, number2):
    # Inicializacion de resultado
    resultado = None

    # Si el usuario desea una suma
    if operacion_mat == SUMA:
        resultado = op.suma(number1, number2)

    # Si el usuario desea una resta
    elif operacion_mat == RESTA:
        resultado = op.resta(number1, number2)

    return resultado


def imprimir_resultado(operacion_mat, resultado):
    if resultado is not None:
        # Si se ha podido realizar la operacion correctamente
        print("El resultado de la {} es: {}".format(operacion_mat, resultado))
    else:
        # Si no se ha indicado correctamente que operacion se quiere hacer salta este error
        error_argumento_operacion()


def error_argumento_operacion():
    # Si no ha indicado que operacion quiere hacer el usuario se le indica el error y salimos con exit()
    print(ERROR_ARGUMENTO_OPERACION + ". " + EJEMPLO_ARGUMENTOS)


def modo_func_argumentos(argumentos):
    # Si hay argumentos entonces entra en modo argumentos el programa
    if len(argumentos) == 4:
        return True
    else:
        return False


def modo_func_inputs(argumentos):
    # Si solo esta el argumento principal (nombre del .py) entonces entra en modo inputs
    if len(argumentos) == 1:
        return True
    else:
        return False


def resultado_final_del_calculo(operacion_mat, number1, number2):
    # Si estan correctas las variables
    if (operacion_mat is not None) and (number1 is not None) and (number2 is not None):
        # Realizar el cálculo
        resultado = seleccionar_operacion(operacion_mat, number1, number2)

        # Imprimir resultado
        imprimir_resultado(operacion_mat, resultado)

    # El programa termina sin mostrar ningún mensaje más
    # Ya se le habrá avisado durante la ejecución de los errores que ha cometido si es necesario


if __name__ == "__main__":
    # Inicializacion de las tres variables del programa
    operacion, num1, num2 = None, None, None
    """ Comprobar si hay argumentos o no
    En caso de haber hacer la suma y resta con esos argumentos, en otro caso pedir al usuario los número"""

    """Si hay cuatro argumentos entonces se entiende que quiere funcionar en modo argumentos
    Si hay un argumemto, se entiende que el usuario quiere que se le pregunte que quiere hacer durante el programa"""

    if modo_func_argumentos(argv):
        # Mensaje explicando al usuario que la calculadora usara los argumentos que ha introducido
        print(MODO_ARGUMENTOS)

        # Manejo de argumentos, aquí esta el control de ValueError
        operacion, num1, num2 = manejo_argumentos(argv)

    elif modo_func_inputs(argv):
        # Mensaje explicando al usuario que la calculadora usara los inputs que introduzca
        print(MODO_INPUTS)

        # Manejo de los inputs, aquí esta el control de ValueError
        operacion, num1, num2 = manejo_inputs()

    else:
        print(ERROR_GENERAL)
        print(EXPLICACION_MODO_ARGUMENTOS + '. ' + EJEMPLO_ARGUMENTOS)
        print(EXPLICACION_MODO_INPUTS)

    """En caso de que la ejecución haya ido correctamente al final del programa se calcula el resultado final 
    y se le informa de cual ha sido el resultado al usuario"""

    # Realizar el cálculo e imprimir los resultados
    resultado_final_del_calculo(operacion, num1, num2)
