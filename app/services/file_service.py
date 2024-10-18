import PyPDF2
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class FileService:
    """
    La clase FileService proporciona métodos para extraer texto de archivos PDF, generar embeddings de oraciones,
    y encontrar las oraciones más relevantes dado un embedding de entrada.
    """
    def __init__(self):
        """
        Inicializa el FileService con un modelo de embeddings de oraciones.
        """
        self.embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def extract_text(self, file_path):
        """
        Extrae el texto de un archivo PDF.

        Args:
            file_path (str): La ruta al archivo PDF del cual extraer el texto.

        Returns:
            str: El texto extraído del PDF, o None si falla la extracción.
        """
        try:
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
                return text
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
            return None

    def generate_embeddings(self, text):
        """
        Genera embeddings de oraciones para el texto dado.

        Args:
            text (str): El texto que se va a dividir en oraciones y para el cual se generarán embeddings.

        Returns:
            tuple: Una lista de oraciones y sus embeddings correspondientes.
        """
        sentences = text.split('. ')
        embeddings = self.embedding_model.encode(sentences)
        return sentences, embeddings

    def find_relevant_sentences(self, question_embedding, sentences_embeddings, sentences, top_k=3):
        """
        Encuentra las oraciones más relevantes a partir de los embeddings dados en base al embedding de una pregunta.

        Args:
            question_embedding (array): El embedding de la pregunta del usuario.
            sentences_embeddings (array): Los embeddings de las oraciones del texto.
            sentences (list): La lista de oraciones.
            top_k (int, optional): El número de oraciones más relevantes a devolver (por defecto es 3).

        Returns:
            list: Las oraciones más relevantes basadas en la similitud coseno.
        """
        similarities = cosine_similarity([question_embedding], sentences_embeddings)[0]
        top_indices = similarities.argsort()[-top_k:][::-1]
        relevant_sentences = [sentences[i] for i in top_indices]
        return relevant_sentences
