"""Modulo que inicia una APU para interactuar con el asistente de IA mediante requests"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.file_service import FileService
from app.services.assistant import Assistant
from app.config import model_type, ai_api_key, pdf_file_path

app = FastAPI()

# Inicializar servicios
file_service = FileService()
text = file_service.extract_text(pdf_file_path)
if text:
    sentences, embeddings = file_service.generate_embeddings(text)
else:
    raise Exception("No se pudo extraer el texto del archivo PDF.")

assistant = Assistant(model_type=model_type, ai_api_key=ai_api_key)

# Contexto de la conversación
conversation_history = [
    {"role": "system", "content": "Eres un asistente útil."}
]

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask(question: Question):
    """
    Endpoint para realizar preguntas al asistente de IA.

    Args:
        question (Question): Pregunta realizada por el usuario.

    Returns:
        dict: Respuesta generada por el asistente.
    """
    user_input = question.question
    if not user_input:
        raise HTTPException(status_code=400, detail="Pregunta no proporcionada.")

    # Generar embedding
    question_embedding = file_service.embedding_model.encode([user_input])[0]

    # Encontrar las oraciones más relevantes del documento
    relevant_sentences = file_service.find_relevant_sentences(question_embedding, embeddings, sentences)

    # Añadir el contexto relevante al historial de la conversación
    context_text = " ".join(relevant_sentences)
    conversation_history.append({"role": "user", "content": user_input})

    if context_text:
        conversation_history.append({"role": "system", "content": f"Contexto relevante del documento: {context_text}"})

    # Obtener la respuesta del asistente
    response = assistant.ask_question(user_input, context=conversation_history)
    conversation_history.append({"role": "assistant", "content": response})

    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)