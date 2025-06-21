# 🚀 AI-Powered Recruiter LinkedIn Post Generator

**Generate professional, engaging, and enhanced LinkedIn posts from any job description in seconds.**  
This project uses the power of **Groq LLM + Langchain + Streamlit** to help recruiters attract top talent effortlessly.
---
## 🌟 Live Demo  
🚀 **Try it out here** 👉 [Recruiter LinkedIn Post Generator](https://recruiter-linkedin-post-generator-jodfpegx9bds96w5pr4yex.streamlit.app/)

---
## ✨ Features
- 📝 **Paste a Job Description**, Get a Polished LinkedIn Post
- 🗣️ **Select Output Tone**: Professional, Friendly, Excited, or Urgent
- 🌍 **Multi-Language Output**: English, Hinglish, Hindi, French
- 🤖 **AI-Generated Hashtags** (4–6 relevant ones)
- 😊 **Emoji-enhanced Descriptions** (to increase engagement)
- 📋 **Copy to Clipboard** with modern UI styling
- 📄 **Download Post as `.txt`**
- 🔢 **Word & Character Counter**
- 💡 Fully built with **Groq API**, **LangChain**, **Streamlit**, and **Dotenv**

---
## 🧠 How It Works

1. You paste a raw job description into the app.
2. You select the desired **tone** and **language**.
3. It builds a smart prompt and sends it to **Groq LLM** using **LangChain**.
4. The AI generates a tailored LinkedIn-style post with hashtags and emojis.
5. You can **copy**, **download**, or **share** the content easily.

---
## 🛠️ Tech Stack

- 🐍 Python 3.11+
- 🧠 Groq LLM via LangChain
- 📦 Streamlit for UI
- 📄 Python-Dotenv for key management
- 📊 Pandas (for future enhancements like analytics)

---
## 📦 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/recruiter-post-generator.git
cd recruiter-post-generator

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
echo "GROQ_API_KEY=your_groq_api_key" > .env

# 5. Run the app
streamlit run main.py
```

---
## 📂 Folder Structure

```
📁 recruiter-post-generator/
├── post_generator.py
├── llm_helper.py
├── main.py
├── requirements.txt
├── .env (excluded from Git)
└── README.md
```

---
## 👨‍💻 Author

**Kurra Srinivas**  
📧 Email: [srinivaskurra886@gmail.com](mailto:srinivaskurra886@gmail.com)  
🔗 LinkedIn: [Kurra Srinivas](https://www.linkedin.com/in/kurra-srinivas-31727420b/)  
🐙 GitHub: [Kurra-Srinivas](https://github.com/Kurra-Srinivas)

---