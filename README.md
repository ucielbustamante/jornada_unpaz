# Proyecto Asistente de IA - Setup Paso a Paso

¡Bienvenidos! Este es un proyecto para que aprendas a crear tu propio asistente de IA. Sigue estos pasos para configurar tu entorno y personalizar tu asistente. No te preocupes, vamos paso a paso, así que solo tienes que seguir las instrucciones

## 1. Realizar un fork del repositorio (crear tu propia copia)

Primero, necesitas hacer una copia del código del proyecto en tu cuenta de GitHub. Esto se llama hacer un "fork".

1. Ve a la página del repositorio en GitHub.

2. Haz clic en el botón "Fork" en la esquina superior derecha. Esto creará una copia del proyecto en tu cuenta de GitHub.

3. Ahora que tienes tu propia copia, vamos a descargar el código del proyecto en tu computadora. Abre una terminal (o el programa que uses para escribir comandos).

4. Clona el repositorio con este comando, reemplazando `tu-usuario` con tu nombre de usuario de GitHub:

   ```bash
   git clone https://github.com/tu-usuario/jornada-unpaz.git
   ```

5. Una vez descargado el proyecto, entra en la carpeta del proyecto:
   ```bash
   cd jornada-unpaz
   ```

## 2. Crear un entorno virtual (aislar las dependencias)

Para que todo funcione bien y evitar problemas con las librerías, vamos a crear un entorno virtual de Python. Este entorno es como un espacio separado donde instalaremos las herramientas necesarias para correr el proyecto.

1. Crea el entorno virtual (esto crea una carpeta llamada venv):

   ```bash
   python -m venv venv
   ```

2. Activa el entorno virtual:

   ```bash
   venv\\Scripts\\activate
   ```

3. Una vez activado el entorno, verás algo como (venv) al inicio de la línea de tu terminal. Ahora instala las librerías que necesita el proyecto usando el archivo requirements.txt:

   ```bash
   pip install -r requirements.txt
   ```

## 3. Configurar las variables y generar un archivo PDF para que la IA lo utilice como referencia
   
   En esta sección, vamos a configurar las variables necesarias y crear un archivo PDF que la inteligencia artificial utilizará como base para generar sus respuestas. Sigue estos pasos:

   1. Configurar las variables: Asegúrate de que todas las variables del proyecto estén correctamente definidas en el archivo app/config.py. Las variables clave que debes verificar son:

      - model_type: El modelo de IA que se utilizará.
      - ai_api_key: Tu clave de acceso a la API.
      - pdf_file_path: La ruta donde se encuentra el archivo PDF que servirá como referencia.

   2. Crear el archivo PDF: Genera un archivo PDF con el contenido que la IA usará como fuente de información. Este documento debe contener el material que el asistente utilizará para dar respuestas basadas en su contenido.

   3. Guardar el archivo PDF: Guarda el PDF en la raíz del proyecto. Asegúrate de que la ruta configurada en la variable pdf_path apunte correctamente al archivo para que la IA pueda acceder a él sin problemas.

## 4. Probar el proyecto (¡hora de la acción!)

Vamos a probar las diferentes partes del proyecto para asegurarnos de que todo funcione correctamente. El proyecto te permite interactuar con un asistente de IA de tres formas: mediante consola, una interfaz gráfica (Streamlit), o una API.

Ejecuta el siguiente comando en la terminal para iniciar el menú:
   ```bash
   python main.py
   ```

### 1. Ejecutar el asistente por consola

   En el menú que aparece, selecciona la opción 3 y presiona Enter. Esto abrirá la consola interactiva, donde podrás hacer preguntas al asistente directamente desde tu terminal.

   Si todo funciona bien, el asistente responderá a tus preguntas en la consola. Si hay algún error, asegúrate de revisar los pasos anteriores para solucionarlo.

### 2. Ejecutar la interfaz gráfica con Streamlit

   Este proyecto cuenta con una interfaz gráfica de chat que se ejecuta en el navegador. Para usarla:

   1. En el menú principal, selecciona la opción 2 y presiona Enter.
   2. Esto abrirá una nueva ventana en tu navegador con la interfaz de chat, donde podrás interactuar con el asistente haciendo preguntas.
### 3. Ejecutar la API

   El proyecto también incluye una API que permite que otros programas interactúen con el asistente. Para probarla:

   1. En el menú, selecciona la opción 1 y presiona Enter.

   2. La API se ejecutará en http://localhost:8000 y estará lista para recibir solicitudes HTTP.

   Además, puedes acceder a la documentación interactiva de la API en: http://localhost:8000/docs.

## 5. Guardar tus cambios y subirlos (commit y push)

Después de haber hecho tus cambios en el asistente, necesitas guardarlos y subirlos a tu espacio en GitHub para que todos puedan verlos.

1. Guarda tus cambios. Primero, añade todos los archivos que cambiaste:

   ```bash
   git add .
   ```

2. Luego, haz un commit. Esto es como poner una etiqueta con una descripción a tus cambios. Escribe un mensaje breve explicando qué has hecho:

   ```bash
   git commit -m "Descripción de los cambios"
   ```

3. Finalmente, sube tus cambios a la rama que creaste antes:

   ```bash
   git push origin nombre-de-tu-rama
   ```


