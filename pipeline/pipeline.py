from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir:str="chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline")
            vector_store = VectorStoreBuilder(csv_path="",persist_dir=persist_dir)

            retriever = vector_store.load_vectorstore().as_retriever()

            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)

            logger.info("Successfully initialize recommendation pipeline")

        except Exception as e:
            logger.error(f"Failed to initialize the recommendation pipeline: str{e}")
            raise CustomException("Error during pipeline initialization", e)
        
    def recommend(self, query:str)->str:
        try:
            logger.info(f"Received user query: {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info(f"Recommendations generated successfully: {recommendation}")
            return recommendation
        
        except Exception as e:
            logger.error(f"Failed to generate the recommendation. {e}")
            raise CustomException("Error during getting recommendation", e)
        