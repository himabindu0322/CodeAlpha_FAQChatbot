import streamlit as st
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data
nltk.download('punkt')

st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- Session State ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Function to clear question input
def clear_input():
    st.session_state["user_input"] = ""

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 50%,
        #334155 100%
    );
    color: white;
}

h1 {
    text-align: center;
    color: #38bdf8 !important;
}

p, label, div {
    color: #e2e8f0 !important;
}

[data-testid="stSidebar"] {
    background: #1e293b;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.stButton > button {
    background: linear-gradient(
        90deg,
        #06b6d4,
        #3b82f6
    ) !important;

    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    height: 50px !important;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    transform: scale(1.03);
    transition: 0.3s;
}

.stTextInput input {
    color: black !important;
    background-color: white !important;
    border-radius: 10px !important;
    border: 2px solid #38bdf8 !important;
}

.stTextInput input::placeholder {
    color: gray !important;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.title("🤖 FAQ Chatbot")
st.write("Ask questions and get instant answers!")

# ---------------- Load FAQ Dataset ----------------
df = pd.read_csv(
    "faq.csv",
    encoding="utf-8",
    quotechar='"',
    on_bad_lines="skip"
)

questions = df["Question"].tolist()
answers = df["Answer"].tolist()

# ---------------- TF-IDF ----------------
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

# ---------------- User Input ----------------
user_question = st.text_input(
    "Ask your question:",
    key="user_input"
)

# ---------------- Buttons ----------------
col1, col2 = st.columns(2)

with col1:
    get_answer = st.button("Get Answer")

with col2:
    st.button(
        "🗑 Clear Question",
        on_click=clear_input
    )

# ---------------- Answer Logic ----------------
if get_answer:

    if user_question.strip() == "":
        st.warning("Please enter a question.")

    else:

        user_vector = vectorizer.transform([user_question])

        similarities = cosine_similarity(
            user_vector,
            question_vectors
        )

        best_match = similarities.argmax()
        score = similarities[0][best_match]

        if score > 0.2:
            answer = answers[best_match]

            st.success("Answer:")
            st.write(answer)

        else:
            answer = "Sorry, I don't know the answer."
            st.error(answer)

        # Save chat history
        st.session_state.chat_history.append({
            "question": user_question,
            "answer": answer
        })

# ---------------- Sidebar Chat History ----------------
st.sidebar.header("💬 Chat History")

if st.sidebar.button("🗑 Clear History"):
    st.session_state.chat_history = []
    st.sidebar.success("History Cleared!")

if len(st.session_state.chat_history) == 0:
    st.sidebar.write("No chats yet.")
else:
    for i, chat in enumerate(
        reversed(st.session_state.chat_history),
        start=1
    ):
        with st.sidebar.expander(
            f"Chat {len(st.session_state.chat_history)-i+1}"
        ):
            st.write(
                f"**Question:** {chat['question']}"
            )
            st.write(
                f"**Answer:** {chat['answer']}"
            )

# ---------------- Footer ----------------
st.markdown("---")
st.caption(
    "Developed for CodeAlpha AI Internship 🚀"
)
