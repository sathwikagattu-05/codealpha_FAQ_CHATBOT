import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer 
import time
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI FAQ Chatbot")

st.markdown(
"""
### Welcome!

Ask questions about our company and I'll answer them instantly.

Powered by **TF-IDF + Cosine Similarity**.
"""
)

st.divider()
with st.sidebar:
    st.title("🤖 AI FAQ Chatbot")

    st.info("An AI-powered FAQ chatbot built using Python, Streamlit, and Scikit-learn.")

    st.divider()

    st.subheader("✨ Features")

    st.write("✅ AI FAQ")
    st.write("💬 Chat History")
    st.write("📥 Download Chat")
    st.write("🧹 Clear Chat")

    st.divider()
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "👋 Hello! I'm your AI FAQ Assistant. Ask me anything about our services!"
            }
        ]
        st.rerun()

        
    
    
if "messages" not in st.session_state:
    st.session_state.messages=[{
            "role": "assistant",
            "content": "👋 Hello! I'm your AI FAQ Assistant. Ask me anything about our services!"
        }]
    

model=SentenceTransformer("all-MiniLM-L6-v2")        
# FAQ Questions
questions = [
    "What are your working hours?",
    "Where are you located?",
    "How can I contact you?",
    "Do you provide online services?",
    "What payment methods do you accept?",
    "Do you offer internships?",
    "Can I visit your office?",
    "What services do you provide?",
    "How long does delivery take?",
    "Do you provide customer support?"
]

answers = [
    "We are open from 9 AM to 6 PM Monday to Saturday.",
    "We are located in Hyderabad.",
    "You can contact us at support@example.com.",
    "Yes, we provide online services across India.",
    "We accept UPI, Credit Card, Debit Card and Net Banking.",
    "Yes, internship opportunities are announced regularly.",
    "Yes, visitors are welcome during working hours.",
    "We provide AI, Software Development and Consulting services.",
    "Delivery usually takes 3 to 5 business days.",
    "Customer support is available 24×7 via email."
]
questions.extend([
    "Who developed this chatbot?",
    "Which programming language is used?",
    "What is AI?",
    "What is machine learning?",
    "Can you help me?"
])

answers.extend([
    "This chatbot was developed by Sathwika Gattu.",
    "This chatbot is built using Python.",
    "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
    "Machine Learning is a branch of AI where systems learn from data.",
    "Yes! I'll answer the questions stored in my knowledge base."
]) 
question_embeddings=model.encode(questions)
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "👤"

    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])
st.subheader("💡 Try asking:")

col1, col2 = st.columns(2)

with col1:
    if st.button("📍 Location"):
        st.session_state.suggested = "Where are you located?"

    if st.button("⏰ Working Hours"):
        st.session_state.suggested = "What are your working hours?"

with col2:
    if st.button("💳 Payment"):
        st.session_state.suggested = "What payment methods do you accept?"

    if st.button("🎓 Internships"):
        st.session_state.suggested = "Do you offer internships?"
user_input = st.chat_input(
    "Ask your question...",
    key="chat_input")

if "suggested" in st.session_state:
    user_input = st.session_state.pop("suggested")

if user_input:
    st.session_state.messages.append( 
        {"role":"user","content":user_input})
    question_embeddings = model.encode(questions)
    start=time.time()
    user_embedding = model.encode([user_input])
    similarity = cosine_similarity(user_embedding, question_embeddings)
    index = similarity.argmax()
    confidence=similarity[0][index]
    st.caption(f"confidence score:{confidence:.2f}")



    if confidence > 0.45:
       with st.spinner("🤖 AI is thinking..."):
        st.session_state.messages.append(
        {"role": "assistant", "content": answers[index]})
        st.rerun()
    else: 
       with st.spinner("🤖 AI is thinking..."):
        st.session_state.messages.append( {
        "role": "assistant",
        "content": "🤔 I couldn't find an answer for that question. Please try asking something related to our FAQs."})
    
    end = time.time()
    st.caption(f"⚡ Response Time: {(end-start):.3f} seconds")
    st.rerun()
if st.session_state.messages:
    chat = ""

    for msg in st.session_state.messages:
        chat += f"{msg['role']}: {msg['content']}\n"

    st.download_button(
        "📥 Download Chat",
        chat,
        file_name="chat_history.txt"
    )    
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric("💬 Total Messages", len(st.session_state.messages))

with col2:
    user_count = sum(1 for msg in st.session_state.messages if msg["role"] == "user")
    st.metric("🙋 Questions Asked", user_count)       