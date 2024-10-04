import os

# Preguntas y respuestas correctas del archivo ansible-navigator.yml (sin espacios para facilitar la validación en las preguntas)
correct_answers_concept = [
    "---",
    "ansible-navigator:",
    "execution-environment:",
    "image:",  # Solo verificaremos la clave "image:"
    "pull:",
    "policy:missing",
    "playbook-artifact:",
    "enable:false",
    "mode:stdout"
]

# Respuestas correctas con indentación para la validación del archivo completo
correct_answers_full = [
    "---",
    "ansible-navigator:",
    "  execution-environment:",
    "    image: utility.lab.example.com/ee-supported-rhel8:latest",  # Aquí va completa
    "    pull:",
    "      policy: missing",
    "  playbook-artifact:",
    "    enable: false",
    "    mode: stdout"
]

def ask_question_concept(question, correct_answer):
    """Función para hacer preguntas y verificar respuestas (sin considerar espacios)"""
    answer = input(question + "\n").replace(" ", "")  # Eliminar espacios en la respuesta
    if answer.strip() == correct_answer:
        print("¡Correcto!\n")
        return True
    else:
        print(f"Incorrecto. La respuesta correcta era: {correct_answer}\n")
        return False

def play_ansible_navigator_quiz():
    """Juego de preguntas sobre la estructura del archivo ansible-navigator.yml"""
    print("¡Bienvenido al juego de configuración del archivo ansible-navigator.yml!\n")
    score = 0

    # Preguntar línea por línea y sumar puntos
    questions = [
        "Escribe la primera línea del archivo (inicia el YAML):",
        "Escribe la segunda línea (definir ansible-navigator):",
        "Escribe la tercera línea (comienza a definir el entorno de ejecución):",
        # Modificamos la cuarta pregunta con una pista
        "Escribe la cuarta línea (imagen del entorno de ejecución) Pista: utility.lab.example.com/ee-supported-rhel8:latest",
        "Escribe la quinta línea (comienza la política de halar):",
        "Escribe la sexta línea (política de pull):",
        "Escribe la séptima línea (comienza la configuración del artefacto del playbook):",
        "Escribe la octava línea (deshabilitar artefactos):",
        "Escribe la novena línea (modo de salida stdout):"
    ]

    for i in range(len(questions)):
        # Para la cuarta línea, se verificará solo "image:"
        if i == 3:
            score += ask_question_concept(questions[i], correct_answers_concept[i])
        else:
            score += ask_question_concept(questions[i], correct_answers_concept[i])

    total_questions = len(questions)
    print(f"Tu puntuación final es: {score}/{total_questions}\n")

    if score == total_questions:
        print("¡Bien hecho! Ahora intenta escribir el archivo completo.\n")
    else:
        print("Buen intento. Ahora prueba a generar el archivo completo para reforzar lo que aprendiste.\n")

def clear_screen():
    """Función para limpiar la pantalla"""
    os.system('cls' if os.name == 'nt' else 'clear')

def evaluate_ansible_navigator_file(user_input):
    """Función que evalúa si el archivo ansible-navigator.yml está correctamente escrito (con indentación)"""
    # Eliminar espacios en blanco y líneas vacías para comparar correctamente
    user_input_cleaned = "\n".join([line.strip() for line in user_input.strip().splitlines() if line.strip()])
    correct_cfg_cleaned = "\n".join([line.strip() for line in "\n".join(correct_answers_full).splitlines() if line.strip()])

    if user_input_cleaned == correct_cfg_cleaned:
        print("¡El archivo ansible-navigator.yml es correcto! ¡Bien hecho!")
    else:
        print("El archivo ansible-navigator.yml tiene algunos errores. Aquí está el archivo correcto:\n")
        print("\n".join(correct_answers_full))

def play_write_ansible_navigator_game():
    """Juego para escribir la estructura completa de ansible-navigator.yml"""
    print("Escribe la estructura completa del archivo ansible-navigator.yml. Imagen: utility.lab.example.com/ee-supported-rhel8:latest (incluyendo todas las líneas y indentación):")
    print("(Cuando termines, escribe 'FIN' y presiona Enter para finalizar)\n")

    user_input = ""
    while True:
        line = input()  # Leer la línea ingresada por el usuario
        if line.strip().lower() == "fin":  # Si el usuario escribe "FIN", terminar
            break
        user_input += line + "\n"  # Agregar las líneas ingresadas

    evaluate_ansible_navigator_file(user_input)

def main_game():
    """Función principal que ejecuta todo el juego"""
    # Paso 1: Cuestionario sobre ansible-navigator.yml
    play_ansible_navigator_quiz()

    # Paso 2: Limpiar pantalla y pedir escribir el archivo completo
    input("Presiona Enter para continuar y escribir el archivo completo...")
    clear_screen()

    # Paso 3: Escribir el archivo completo
    play_write_ansible_navigator_game()

    # Paso 4: Feedback final
    print("\nGracias por jugar. ¡Sigue practicando para mejorar tu memoria!")

# Ejecutar el juego
main_game()

