# Función para cifrar una sola letra

def cifrar_letra(letra, desplazamiento):

    # Comprobamos que el desplazamiento sea válido
    if desplazamiento < 1 or desplazamiento > 25:
        raise ValueError("El desplazamiento debe estar entre 1 y 25.")

    # Convertimos la letra a número (ASCII)
    codigo = ord(letra)

    # Aplicamos el desplazamiento con rotación
    nuevo_codigo = ((codigo - 65 + desplazamiento) % 26) + 65

    # Volvemos a convertir a letra
    return chr(nuevo_codigo)


# Función para descifrar una letra
def descifrar_letra(letra, desplazamiento):
    return cifrar_letra(letra, 26 - desplazamiento)



# Función para cifrar un mensaje completo

def cifrar_mensaje(mensaje, desplazamiento):

    mensaje = mensaje.upper()  # Pasamos todo a mayúsculas
    resultado = ""

    for caracter in mensaje:
        if caracter.isalpha():  # Solo ciframos letras
            resultado += cifrar_letra(caracter, desplazamiento)
        else:
            resultado += caracter  # Lo demás se queda igual

    return resultado


# Función para descifrar un mensaje completo
def descifrar_mensaje(mensaje, desplazamiento):

    resultado = ""

    for caracter in mensaje:
        if caracter.isalpha():
            resultado += descifrar_letra(caracter, desplazamiento)
        else:
            resultado += caracter

    return resultado


# Programa principal

print("=== CIFRADO CÉSAR ===")

mensaje = input("Introduce el mensaje: ")

# Pedimos desplazamiento y comprobamos que sea correcto
while True:
    try:
        desplazamiento = int(input("Introduce el desplazamiento (1-25): "))
        if 1 <= desplazamiento <= 25:
            break
        else:
            print("Debe estar entre 1 y 25.")
    except ValueError:
        print("Introduce un número válido.")

# Ciframos
mensaje_cifrado = cifrar_mensaje(mensaje, desplazamiento)
print("\nMensaje cifrado:", mensaje_cifrado)

# Desciframos para comprobar
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, desplazamiento)
print("Mensaje descifrado:", mensaje_descifrado)