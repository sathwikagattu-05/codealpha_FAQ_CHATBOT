# 🤖 AI FAQ Chatbot

An AI-powered FAQ Chatbot built using **Python**, **Streamlit**, and **Scikit-learn**. The chatbot answers frequently asked questions by finding the most similar question using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🚀 Features

- 💬 Chat-style interface
- 🤖 AI and User avatars
- 📜 Chat history
- 🧹 Clear chat option
- 📥 Download chat history
- 📊 Chat statistics
- 👋 Welcome message
- 📚 Multiple FAQs with intelligent matching
- ⚡ Fast responses
- 🎨 Clean and responsive Streamlit UI

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

---

## 📂 Project Structure

```
CodeAlpha_FAQ_Chatbot/
│── app.py
│── requirements.txt
│── README.md
```

---

## ▶️ Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_FAQ_Chatbot.git
```

2. Navigate to the project folder:

```bash
cd CodeAlpha_FAQ_Chatbot
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. The user enters a question.
2. The chatbot converts all FAQ questions and the user's question into TF-IDF vectors.
3. Cosine Similarity is used to find the most similar FAQ.
4. If the similarity score is above a threshold, the corresponding answer is displayed.
5. Otherwise, the chatbot informs the user that no suitable answer was found.

---

## 🌐 Live Demo

Add your Streamlit deployment link here:

https://YOUR-STREAMLIT-APP.streamlit.app

---

## 📸 Screenshot

Add a screenshot of your chatbot here.

Example:

```
![Chatbot Screenshot](screenshot.png)
```

---

## 👩‍💻 Developer

**Sathwika Gattu**

Built as part of the **CodeAlpha Artificial Intelligence Internship**.

---

## 📜 License

This project is developed for educational and internship purposes.