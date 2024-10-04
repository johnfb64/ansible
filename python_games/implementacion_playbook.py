import os

# Preguntas y respuestas clave sobre comandos de Ansible para inventarios
questions = [
    {
        "question": "¿Qué comando muestra el inventario completo de Ansible?",
        "answer": "ansible-navigator inventory -i inventory -m stdout --list",
        "output": """
EXAMPLE OUTPUT:
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    }
}
        """
    },
    {
        "question": "¿Qué comando permite consultar la información de un host específico en Ansible?",
        "answer": "ansible-navigator inventory -i inventory -m stdout --host <host_name>",
        "output": """
EXAMPLE OUTPUT:
{
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "host": "server1.example.com",
    "groups": ["all", "web"]
}
        """
    },
    {
        "question": "¿Qué comando muestra un gráfico de los grupos en el inventario de Ansible?",
        "answer": "ansible-navigator inventory -i inventory -m stdout --graph <grupo>",
        "output": """
EXAMPLE OUTPUT:
@all:
  |--@ungrouped:
  |--@web:
      |--web1.example.com
      |--web2.example.com
        """
    },
    {
        "question": "¿Qué comando permite explorar el inventario de manera interactiva?",
        "answer": "ansible-navigator inventory -i inventory",
        "output": """
EXAMPLE OUTPUT:
Interactive mode launched. Use the menu to explore hosts, groups, and variables interactively.
        """
    },
    {
        "question": "¿Cómo cambiar la ubicación del archivo de inventario para Ansible Navigator?",
        "answer": "ansible-navigator -i /ruta/a/inventario",
        "output": """
EXAMPLE OUTPUT:
Custom inventory from /ruta/a/inventario loaded successfully.
        """
    },
    {
        "question": "¿Qué comando utilizas para limpiar el caché de inventario?",
        "answer": "ansible-inventory --flush-cache",
        "output": """
EXAMPLE OUTPUT:
Cache for inventory flushed successfully.
        """
    }
]

def clear_screen():
    """Función para limpiar la pantalla"""
    os.system('cls' if os.name == 'nt' else 'clear')

def normalize_answer(answer):
    """Función para normalizar las respuestas ignorando los valores específicos de host, grupo y rutas"""
    normalized = answer.lower()

    # Ignorar el valor después de --host, --graph o -i, porque puede ser cualquier cosa
    if "--host" in normalized:
        normalized = normalized.split("--host")[0] + "--host <valor>"
    if "--graph" in normalized:
        normalized = normalized.split("--graph")[0] + "--graph <valor>"
    if "-i" in normalized:
        normalized = normalized.split("-i")[0] + "-i <ruta>"

    # Reemplazar <host_name> o <grupo> o <ruta> en la respuesta correcta
    normalized = normalized.replace("<host_name>", "<valor>")
    normalized = normalized.replace("<grupo>", "<valor>")
    normalized = normalized.replace("<ruta>", "<valor>")

    return normalized

def ask_question(question_data):
    """Función para hacer una pregunta, verificar la respuesta y mostrar salida ficticia"""
    print(question_data["question"])
    answer = input("Escribe tu respuesta: ").strip().lower()

    # Normalizar las respuestas del usuario y la respuesta correcta
    normalized_answer = normalize_answer(answer)
    normalized_correct_answer = normalize_answer(question_data["answer"].lower())
    
    if normalized_answer == normalized_correct_answer:
        print("¡Correcto!\n")
        print(f"Salida ficticia del comando:\n{question_data['output']}\n")
        return True
    else:
        print(f"Incorrecto. La respuesta correcta era:\n{question_data['answer']}\n")
        return False

def play_ansible_inventory_quiz():
    """Juego de preguntas sobre comandos de inventarios en Ansible"""
    print("¡Bienvenido al juego de comandos sobre Inventarios en Ansible!\n")
    score = 0
    total_questions = len(questions)

    # Preguntar una por una y sumar puntos por respuestas correctas
    for question_data in questions:
        if ask_question(question_data):
            score += 1
        # Limpiar la pantalla después de cada pregunta
        input("\nPresiona Enter para continuar a la siguiente pregunta...")
        clear_screen()

    # Mostrar el puntaje final
    print(f"\nTu puntuación final es: {score}/{total_questions}\n")

    if score == total_questions:
        print("¡Excelente! ¡Conoces muy bien los comandos de Ansible para inventarios!")
    elif score >= total_questions * 0.7:
        print("¡Buen trabajo! Pero podrías mejorar en algunos comandos.")
    else:
        print("Sigue practicando para mejorar tu conocimiento sobre los comandos de inventarios en Ansible.")

def main_game():
    """Función principal que ejecuta el juego"""
    # Paso 1: Iniciar el juego de preguntas
    play_ansible_inventory_quiz()

    # Paso 2: Finalizar
    print("\nGracias por jugar. ¡Sigue practicando para mejorar tus conocimientos sobre Ansible!")

# Ejecutar el juego
if __name__ == "__main__":
    main_game()

