"""Modulo que inicia una aplicacion streamlit para interactuar con el asistente de IA"""
import streamlit as st
from services.assistant import Assistant
from services.file_service import FileService
from config import model_type, ai_api_key, pdf_file_path

def main():
    """
    Función principal que crea la interfaz web con Streamlit para interactuar con el asistente de IA.
    """
    st.title("Asistente de IA")

    # Ruta al PDF de configuración

    # Inicializar el asistente y el servicio de archivos en el estado de sesión
    if 'assistant' not in st.session_state:
        st.session_state['assistant'] = Assistant(model_type=model_type, ai_api_key=ai_api_key)

    if 'file_service' not in st.session_state:
        st.session_state['file_service'] = FileService()
        text = st.session_state['file_service'].extract_text(pdf_file_path)
        if text:
            sentences, embeddings = st.session_state['file_service'].generate_embeddings(text)
            st.session_state['sentences'] = sentences
            st.session_state['embeddings'] = embeddings
            st.write("Embeddings generados.")
        else:
            st.write("No se pudo extraer el texto del archivo.")

    if 'conversation_history' not in st.session_state:
        st.session_state['conversation_history'] = []

    # Entrada del usuario
    user_input = st.text_input("Haz una pregunta:")

    if st.button("Enviar"):
        if user_input:
            # Generar el embedding de la pregunta del usuario
            question_embedding = st.session_state['file_service'].embedding_model.encode([user_input])[0]

            # Encontrar las oraciones más relevantes del documento
            relevant_sentences = st.session_state['file_service'].find_relevant_sentences(
                question_embedding,
                st.session_state['embeddings'],
                st.session_state['sentences']
            )

            # Añadir el contexto relevante al historial de la conversación
            context_text = " ".join(relevant_sentences)
            st.session_state['conversation_history'].append({"role": "user", "content": user_input})

            # Obtener la respuesta del asistente
            response = st.session_state['assistant'].ask_question(
                user_input,
                context=st.session_state['conversation_history'],
                additional_context=context_text
            )

            # Actualizar el historial de la conversación
            st.session_state['conversation_history'].append({"role": "assistant", "content": response})

            # Mostrar el historial de la conversación
            for message in st.session_state['conversation_history']:
                if message['role'] == 'user':
                    st.markdown(f"**Usuario:** {message['content']}")
                elif message['role'] == 'assistant':
                    st.markdown(f"**Asistente:** {message['content']}")
        else:
            st.write("Por favor, ingresa una pregunta.")

if __name__ == '__main__':
    main()