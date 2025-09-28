from ..LLMInterface import LLMInterface
from ..LLMEnums import IntFloatEnums
import logging
from sentence_transformers import SentenceTransformer
from helpers.config import get_settings

class IntFloatEmbederProvider():

    def __init__(self, default_input_max_characters: int = 1000,):
        self.settings = get_settings()
        self.model = SentenceTransformer(self.settings.EMBEDDING_MODEL_ID, cache_folder=self.settings.EMBEDDING_MODEL_PATH)
        self.default_input_max_characters = default_input_max_characters
        
        self.embedding_model_id = None
        self.embedding_size = None

        self.enums = IntFloatEnums
        self.logger = logging.getLogger(__name__)

    def set_embedding_model(self, model_id: str, embedding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size
    
    def process_text(self, text: str):
        return text[:self.default_input_max_characters].strip()

    def embed_text(self, text: str, document_type: str = None):
        text = self.process_text(text)

        if not self.model:
            self.logger.error("IntFloat client was not set")
            return None

        if document_type == "document":
            response = self.model.encode(
                f"{self.enums.PASSAGE}{text}",
                normalize_embeddings=True
            )
        elif document_type == "query":
            response = self.model.encode(
                f"{self.enums.QUERY}{text}",
                normalize_embeddings=True
            )

        if not response[0]:
            self.logger.error("Error while embedding text with IntFloat")
            return None

        return response