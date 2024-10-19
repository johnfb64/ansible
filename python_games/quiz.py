#!/usr/bin/env python3

import os
import random
import time

# Definir la lista de preguntas y respuestas
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
        "question": "¿Qué comando se utiliza para ver los facts del localhost en Ansible?",
        "answer": "ansible localhost -m ansible.builtin.setup | less",
        "output": """
EXAMPLE OUTPUT:
ansible_facts: {
    "distribution": "CentOS",
    "distribution_version": "8",
    "hostname": "localhost",
    "interfaces": ["eth0"],
    ...
}
        """
    },
    {
        "question": "¿Cómo se edita un archivo secreto con Ansible Vault?",
        "answer": "ansible-vault edit secret.yml",
        "output": """
EXAMPLE OUTPUT:
Archivo secreto descifrado y listo para edición.
        """
    },
    {
        "question": "¿Cómo se resuelven errores de sintaxis con Vault en Ansible?",
        "answer": """ansible-navigator run -m stdout --pae false create_users.yml --syntax-check --vault-id @prompt""",
        "output": """
EXAMPLE OUTPUT:
No se encontraron errores de sintaxis.
        """
    },
    {
        "question": "¿Cómo se ejecuta un playbook con una contraseña de Vault almacenada en un archivo?",
        "answer": """ansible-navigator run -m stdout create_users.yml --vault-password-file=vault-pass""",
        "output": """
EXAMPLE OUTPUT:
Playbook ejecutado correctamente con secretos descifrados.
        """
    },
    {
        "question": "¿Cuál es la configuración mínima recomendada para trabajar con archivos YAML en Vim?",
        "answer": """set et\nset ts=2 sw=2 sts=2\nset nu\nset cuc""",
        "output": """
EXAMPLE OUTPUT:
# Estas configuraciones permiten:
- Convertir tabulaciones en espacios (fundamental en YAML).
- Establecer la indentación a 2 espacios (convención en YAML).
- Habilitar la numeración de líneas y mostrar la columna del cursor.
        """
    },
    # Nueva pregunta sobre la estructura de ansible-navigator.yml
    {
        "question": "¿Cómo es la estructura mínima de un archivo ansible-navigator.yml?",
        "answer": """navigator:\n  mode: interactive\n  container-engine: podman\n  execution-environment:\n    enabled: true\n  ansible:\n    config: ansible.cfg\n    playbook-artifact:\n      enable: true\n      save-as: playbook_artifact.json\n    display:\n      color: true\n  logging:\n    append: true\n    file: /tmp/navigator.log\n    level: info\n  inventory:\n    entries:\n      - inventory.yml""",
        "output": """
EXAMPLE OUTPUT:
---
navigator:
  mode: interactive
  container-engine: podman
  execution-environment:
    enabled: true
  ansible:
    config: ansible.cfg
    playbook-artifact:
      enable: true
      save-as: playbook_artifact.json
    display:
      color: true
  logging:
    append: true
    file: /tmp/navigator.log
    level: info
  inventory:
    entries:
      - inventory.yml
        """
    }
]

# Mejora: Resaltar texto con colores usando ANSI escape codes
def colored_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

def clear_screen():
    """Función para limpiar la pantalla en Linux"""
    os.system('clear')

# Mejora: Quitar el mensaje de ejemplo de respuesta
def display_help_message():
    print("Por favor, responde utilizando el formato adecuado.\n")

# Mejora: Validación flexible de las respuestas
def normalize_answer(answer):
    """Función para normalizar las respuestas"""
    normalized = answer.lower().strip()
    if "--host" in normalized:
        normalized = normalized.split("--host")[0] + "--host <valor>"
    if "--graph" in normalized:
        normalized = normalized.split("--graph")[0] + "--graph <valor>"
    if "-i" in normalized:
        normalized = normalized.split("-i")[0] + "-i <ruta>"
    return normalized

# Validación de la respuesta
def is_answer_correct(user_answer, correct_answer):
    return normalize_answer(user_answer) == normalize_answer(correct_answer)

def ask_question(question_data, time_limit=60):
    """Función para hacer una pregunta y verificar la respuesta"""
    print(question_data["question"])
    display_help_message()
    start_time = time.time()  # Empieza el temporizador

    try:
        # Espera la respuesta del usuario
        answer = input(f"Tienes {time_limit} segundos para responder: ").strip().lower()

        if time.time() - start_time > time_limit:
            print(colored_text("¡Tiempo agotado!\n", "red"))
            return False

        # Verifica la respuesta
        if is_answer_correct(answer, question_data["answer"]):
            print(colored_text("¡Correcto!\n", "green"))
            print(f"Salida ficticia del comando:\n{question_data['output']}\n")
            return True
        else:
            print(colored_text(f"Incorrecto. La respuesta correcta era:\n{question_data['answer']}\n", "red"))
            return False
    except Exception as e:
        print(colored_text(f"Hubo un error: {e}", "red"))
        return False

def repeat_incorrect_questions(incorrect_questions):
    """Función para repetir las preguntas incorrectas si el usuario lo desea"""
    repeat = input(colored_text("\n¿Quieres repetir las preguntas incorrectas? (sí/no): ", "yellow")).strip().lower()
    if repeat in ['sí', 'si']:
        for question_data in incorrect_questions:
            correct = ask_question(question_data)
            input("\nPresiona Enter para continuar...")
            clear_screen()

def play_ansible_inventory_quiz():
    """Juego de preguntas sobre comandos de inventarios en Ansible"""
    print("¡Bienvenido al juego de comandos sobre Inventarios en Ansible!\n")
    score = 0
    total_questions = len(questions)

    # Mezclar preguntas para que sean aleatorias
    random.shuffle(questions)

    incorrect_answers = []  # Mejora: Almacenar respuestas incorrectas

    # Preguntar una por una y sumar puntos por respuestas correctas
    for question_data in questions:
        correct = ask_question(question_data)
        if correct:
            score += 1
        else:
            incorrect_answers.append(question_data)

        input("\nPresiona Enter para continuar a la siguiente pregunta...")
        clear_screen()

    # Mostrar el puntaje final
    print(f"\nTu puntuación final es: {score}/{total_questions}\n")

    # Mejora: Mostrar resumen de respuestas incorrectas
    if incorrect_answers:
        print(colored_text("Resumen de preguntas incorrectas:\n", "yellow"))
        for question in incorrect_answers:
            print(f"- {question['question']}")

        # Repetir preguntas incorrectas si el usuario lo desea
        repeat_incorrect_questions(incorrect_answers)

    if score == total_questions:
        print(colored_text("¡Excelente! ¡Conoces muy bien los comandos de Ansible para inventarios!", "green"))
    elif score >= total_questions * 0.7:
        print(colored_text("¡Buen trabajo! Pero podrías mejorar en algunos comandos.", "yellow"))
    else:
        print(colored_text("Sigue practicando para mejorar tu conocimiento sobre los comandos de inventarios en Ansible.", "red"))

def main_game():
    """Función principal que ejecuta el juego"""
    play_ansible_inventory_quiz()
    print("\nGracias por jugar. ¡Sigue practicando para mejorar tus conocimientos sobre Ansible!")

if __name__ == "__main__":
    main_game()

