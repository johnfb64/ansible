import os

def ask_question(question, correct_answer):
    """Función para hacer preguntas y verificar respuestas"""
    answer = input(question + "\n")
    if answer.strip() == correct_answer:
        print("¡Correcto!\n")
        return True
    else:
        print(f"Incorrecto. La respuesta correcta era: {correct_answer}\n")
        return False

def play_ansible_quiz():
    """Juego de preguntas sobre la estructura del archivo ansible.cfg"""
    print("¡Bienvenido al juego de Ansible Configuración!\n")
    score = 0

    # Preguntas sobre la sección defaults
    score += ask_question("¿Cuál es el archivo por defecto para el inventario en ansible.cfg?", "inventory = ./inventory")
    score += ask_question("¿Cuál es el usuario remoto que Ansible usará por defecto?", "remote_user = user")
    score += ask_question("¿Debes pedir la contraseña para SSH? (Escribe la opción correcta)", "ask_pass = false")

    # Preguntas sobre la sección privilege escalation
    score += ask_question("¿Se debe habilitar la escalación de privilegios?", "become = true")
    score += ask_question("¿Qué método de escalación de privilegios se debe usar?", "become_method = sudo")
    score += ask_question("¿A qué usuario se debe escalar cuando se usen privilegios elevados?", "become_user = root")
    score += ask_question("¿Debes pedir la contraseña al escalar privilegios?", "become_ask_pass = false")

    # Mostrar el puntaje
    total_questions = 7
    print(f"Tu puntuación final es: {score}/{total_questions}\n")

    if score == total_questions:
        print("¡Bien hecho! Ahora prueba a generar el archivo completo.\n")
    else:
        print("Buen intento. Ahora prueba a generar el archivo completo para reforzar lo que aprendiste.\n")

def clear_screen():
    """Función para limpiar la pantalla en Linux"""
    os.system('clear')

def evaluate_ansible_cfg(user_input):
    """Función que evalúa si el archivo ansible.cfg está correctamente escrito"""
    correct_ansible_cfg = """
[defaults]
inventory = ./inventory
remote_user = user
ask_pass = false

[privilege escalation]
become = true
become_method = sudo
become_user = root
become_ask_pass = false
"""
    # Eliminar espacios en blanco y líneas vacías para evitar errores de comparación
    user_input_cleaned = "\n".join([line.strip() for line in user_input.strip().splitlines() if line.strip()])
    correct_cfg_cleaned = "\n".join([line.strip() for line in correct_ansible_cfg.strip().splitlines() if line.strip()])

    if user_input_cleaned == correct_cfg_cleaned:
        print("¡El archivo ansible.cfg es correcto! ¡Bien hecho!")
    else:
        print("El archivo ansible.cfg tiene algunos errores. Aquí está el archivo correcto:\n")
        print(correct_ansible_cfg)

def play_write_ansible_cfg_game():
    """Juego para que escribas la estructura completa de ansible.cfg"""
    print("Escribe la estructura completa del archivo ansible.cfg (incluyendo secciones y valores):")
    print("(Cuando termines, escribe 'FIN' y presiona Enter para finalizar)\n")

    user_input = ""
    while True:
        line = input()  # Lee la línea ingresada por el usuario
        if line.strip().lower() == "fin":  # Si el usuario escribe "FIN", termina
            break
        user_input += line + "\n"  # Continúa agregando las líneas ingresadas

    evaluate_ansible_cfg(user_input)

def main_game():
    """Función principal que ejecuta todo el juego"""
    # Paso 1: Cuestionario sobre ansible.cfg
    play_ansible_quiz()

    # Paso 2: Limpiar pantalla y pedir escribir el archivo
    input("Presiona Enter para continuar y escribir el archivo completo...")
    clear_screen()

    # Paso 3: Escribir el archivo completo
    play_write_ansible_cfg_game()

    # Paso 4: Feedback final
    print("\nGracias por jugar. ¡Sigue practicando para mejorar tu memoria!")

# Ejecutar el juego
main_game()

