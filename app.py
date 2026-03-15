import streamlit as st
from model import prepare_model, recommend

# Configure page settings first
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Cache model for speed
# -----------------------------
@st.cache_resource(show_spinner="Loading the library database...")
def load_model():
    return prepare_model()

# Load data
pt, similarity, popular = load_model()

# -----------------------------
# Main Header
# -----------------------------
st.title("📚 AI Book Recommendation System")
st.markdown("Discover your next great read based on your favorites.")
st.divider()

# -----------------------------
# App Layout: Using Tabs for better organization
# -----------------------------
tab1, tab2 = st.tabs(["🔎 Get Recommendations", "🔥 Popular Books"])

# --- TAB 1: Recommendations ---
with tab1:
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.subheader("Find Similar Books")
        book_list = pt.index.values
        selected_book = st.selectbox("Select a book you enjoyed:", book_list)
        
        # Use primary button color and full width
        submit = st.button("Recommend", type="primary", use_container_width=True)
        
    with col2:
        if submit:
            with st.spinner("Finding the best matches..."):
                recommendations = recommend(selected_book, pt, similarity)
                
                if recommendations:
                    st.success(f"Because you liked **{selected_book}**, you might enjoy:")
                    
                    # Display recommendations in clean message blocks
                    for idx, book in enumerate(recommendations):
                        st.info(f"**{idx + 1}.** {book}")
                else:
                    st.warning("No recommendations found for this book.")
        else:
            # Placeholder text before search
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.write("👈 Select a book from the menu and click **Recommend** to see results here.")

# --- TAB 2: Popular Books ---
with tab2:
    st.subheader("Trending Right Now")
    
    top_books = popular.head(10)
    
    # Create a 5-column grid layout for the top 10 books (2 rows)
    cols = st.columns(5)
    
    for i in range(10):
        # Distribute books across the 5 columns
        with cols[i % 5]:
            # Use a container border to simulate a "Book Card" UI
            with st.container(border=True):
                st.write(f"📖 **{top_books.iloc[i]['Book-Title']}**")
                
                # Optional: If your dataset has an Image-URL column, uncomment the line below
                # st.image(top_books.iloc[i]['Image-URL-M'], use_column_width=True)