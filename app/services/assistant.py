import openai
from groq import Groq

class Assistant:
    """
    La clase Assistant proporciona una forma de interactuar con diferentes modelos de IA (OpenAI o Groq).
    Permite generar respuestas basadas en una pregunta del usuario y en el contexto dado.
    """
    def __init__(self, model_type="openai", ai_api_key=None):
        """
        Inicializa el asistente con el tipo de modelo dado y la clave API.

        Args:
            model_type (str): El tipo de modelo a usar (por ejemplo, "openai" o "groq").
            ai_api_key (str): La clave API para acceder al modelo de IA.
        """
        self.model_type = model_type
        self.ai_api_key = ai_api_key

        if self.model_type == "openai":
            if not self.ai_api_key:
                raise ValueError("Se necesita una API Key de OpenAI para usar este asistente.")
            openai.api_key = self.ai_api_key
        elif self.model_type == "groq":
            if not self.ai_api_key:
                raise ValueError("Se necesita una API Key de Groq para usar este asistente.")
            self.client = Groq(api_key=self.ai_api_key)
        else:
            raise ValueError("Tipo de modelo no soportado.")

    def ask_question(self, question, context=None, additional_context=""):
        """
        Genera una respuesta a la pregunta dada utilizando el modelo de IA especificado.

        Args:
            question (str): La pregunta del usuario a responder.
            context (list, optional): Una lista de mensajes previos para mantener el contexto.
            additional_context (str, optional): Información contextual adicional para ayudar a la IA.

        Returns:
            str: La respuesta generada por el modelo de IA.
        """
        if self.model_type == "openai":
            return self._ask_openai(question, context, additional_context)
        elif self.model_type == "groq":
            return self._ask_groq(question, context, additional_context)
        else:
            raise ValueError("Modelo no soportado para hacer preguntas.")

    def _ask_openai(self, question, context=None, additional_context=""):
        """
        Genera una respuesta utilizando la API de OpenAI en base a la pregunta y el contexto proporcionados.

        Args:
            question (str): La pregunta del usuario.
            context (list, optional): Una lista de mensajes previos para el contexto.
            additional_context (str, optional): Contexto extra a incluir en la conversación.

        Returns:
            str: La respuesta del modelo de OpenAI.
        """
        messages = context.copy() if context else []
        if additional_context:
            messages.append({"role": "system", "content": additional_context})
        messages.append({"role": "user", "content": question})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response['choices'][0]['message']['content']

    def _ask_groq(self, question, context=None, additional_context=""):
        """
        Genera una respuesta utilizando la API de Groq en base a la pregunta y el contexto proporcionados.

        Args:
            question (str): La pregunta del usuario.
            context (list, optional): Una lista de mensajes previos para el contexto.
            additional_context (str, optional): Contexto extra a incluir en la conversación.

        Returns:
            str: La respuesta del modelo de Groq.
        """
        messages = context.copy() if context else []
        if additional_context:
            messages.append({"role": "system", "content": additional_context})
        messages.append({"role": "user", "content": question})

        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False
        )
        return chat_completion.choices[0].message.content