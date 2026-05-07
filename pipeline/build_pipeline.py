from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv
load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline")
        loader = AnimeDataLoader("data/anime_with_synopsis.csv","data/anime_with_synopsis_processed.csv")

        processed = loader.load_and_process()

        vector_store = VectorStoreBuilder(csv_path=processed)
        vector_store.create_and_save_vectorstore()
        logger.info("Successfully created vector store")

        logger.info("Built pipeline successfully")

    except Exception as e:
        logger.error(f"Failed to build the pipeline: str{e}")
        raise CustomException("Error during building pipeline", e)
    
if __name__ == "__main__":
    main()
    