import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide")

load_dotenv()

@st.cache_resource
def initialize_pipeline():
    return AnimeRecommendationPipeline()

pipeline = initialize_pipeline()

st.title("Anime Recommendation System")

query = st.text_input(label="Enter your anime preferences. eg.: A light hearted anime with school settings")

if query:
    with st.spinner("Fetching recommendations for you...", show_time=True):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations:")
        st.write(response)