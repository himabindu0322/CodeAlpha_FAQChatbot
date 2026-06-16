# 🤖 CodeAlpha FAQ Chatbot

A smart and interactive FAQ Chatbot developed using **Python, Streamlit, NLP, and Scikit-Learn**. The chatbot answers user queries by finding the most relevant FAQ using **TF-IDF Vectorization** and **Cosine Similarity**.

## 🚀 Features

* 🔍 Intelligent FAQ matching using NLP
* 🤖 Chatbot interface with Streamlit
* 💬 Chat History stored during the session
* 🗑 Clear Question button
* 🗂 Clear Chat History feature
* 🎨 Professional dark-themed UI
* 📊 TF-IDF Vectorization
* 📈 Cosine Similarity for question matching
* ⚡ Fast and lightweight

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NLTK
* Scikit-Learn

## 📁 Project Structure

```text
CodeAlpha_FAQChatbot/
│
├── app.py
├── faq.csv
├── requirements.txt

```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/CodeAlpha_FAQChatbot.git
cd CodeAlpha_FAQChatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📚 Dataset

The chatbot uses a custom `faq.csv` dataset containing questions and answers from multiple domains such as:

* Artificial Intelligence
* Web Development
* Programming
* Databases
* Cloud Computing
* Cybersecurity
* Data Science

## 🧠 Working Principle

1. Load FAQ dataset from `faq.csv`
2. Convert questions into TF-IDF vectors
3. Accept user input
4. Compute cosine similarity
5. Return the most relevant answer
6. Store conversation in chat history

## 🎯 Internship Task

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship**.

## 👩‍💻 Author

**Himabindu**

## 📜 License

This project is open-source and available for educational purposes.
