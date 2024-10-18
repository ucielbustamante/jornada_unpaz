"""Modulo que inicia una aplicacion en la consola para interactuar con el asistente de IA"""
from services.file_service import FileService
from services.assistant import Assistant
from config import model_type, ai_api_key, pdf_file_path

def run():
    """
    Ejecuta la aplicación en modo consola para interactuar con el asistente de IA.
    """
    print("Bienvenido al asistente de IA. Escribe 'salir' para terminar.")

    # Inicializar el servicio de archivos y el asistente
    file_service = FileService()
    text = file_service.extract_text(pdf_file_path)

    if text:
        sentences, embeddings = file_service.generate_embeddings(text)
    else:
        print("No se pudo extraer el texto del archivo.")
        return

    assistant = Assistant(model_type=model_type, ai_api_key=ai_api_key)

    # Lista para mantener el contexto de la conversación
    conversation_history = [
        {"role": "system", "content": "Eres un asistente útil."}
    ]

    while True:
        # Solicitar la entrada del usuario
        user_input = input("Haz una pregunta (o escribe 'salir' para terminar): ")
        if user_input.lower() == "salir":
            print("Saliendo del programa...")
            break

        # Generar el embedding de la pregunta del usuario
        question_embedding = file_service.embedding_model.encode([user_input])[0]

        # Encontrar las oraciones más relevantes del documento
        relevant_sentences = file_service.find_relevant_sentences(question_embedding, embeddings, sentences)

        # Añadir el contexto relevante al historial de la conversación
        context_text = " ".join(relevant_sentences)
        conversation_history.append({"role": "user", "content": user_input})

        if context_text:
            aditional_context = context_text
        else:
            additional_context = ""
        # Obtener la respuesta del asistente
        response = assistant.ask_question(user_input, context=conversation_history, additional_context=aditional_context)
        print(conversation_history)
        print(relevant_sentences)
        print("Respuesta del asistente:", response)

        # Añadir la respuesta del asistente al historial de la conversación
        conversation_history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    run()