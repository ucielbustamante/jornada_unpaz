import subprocess

def main():
    """
    Función principal para ejecutar diferentes componentes de la aplicación.
    Permite al usuario seleccionar entre levantar la API, la interfaz web, o la consola interactiva.
    """
    print("Selecciona una opción:")
    print("1. Levantar la API")
    print("2. Ejecutar la interfaz web (Streamlit)")
    print("3. Ejecutar la consola interactiva")
    choice = input("Ingresa el número de tu elección: ")

    if choice == '1':
        print("Iniciando la API...")
        subprocess.run(['uvicorn', 'app.api_app:app', '--host', '0.0.0.0', '--port', '8000', '--reload'])
    elif choice == '2':
        print("Iniciando la interfaz web con Streamlit...")
        subprocess.run(['streamlit', 'run', 'app/streamlit_app.py'])
    elif choice == '3':
        print("Ejecutando la consola interactiva...")
        import console_app as console_app
        console_app.run()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()