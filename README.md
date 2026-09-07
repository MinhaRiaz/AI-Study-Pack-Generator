# 📚 AI Study Pack Generator

An interactive **AI-powered Study Pack Generator** built with **Python and Streamlit**. It uses a **multi-stage AI workflow** to transform a study topic, learning goal, education level, and available study duration into a personalized study pack.

The application generates structured **study plans, detailed notes, flashcards, MCQs, exam tips, and quality-reviewed learning content** through a sequential 5-stage AI pipeline.

🚀 **[Try the Live Application](https://ai-study-pack-generator-app.streamlit.app/)**

---

## ✨ Features

### 🎯 5-Stage AI Workflow

Unlike applications that use a single AI prompt, this project uses a **sequential multi-stage workflow** where each stage receives relevant context from the previous stage.

The workflow consists of:

1. **Planning**
   Creates personalized learning objectives, topics, time allocation, difficulty level, and study strategy.

2. **Content Generation**
   Generates structured study notes, explanations, key points, examples, and important terminology.

3. **Assessment**
   Creates assessment material such as MCQs, short-answer questions, and statement verification questions based on the generated content.

4. **Quality Review**
   Reviews the generated material for factual accuracy, pedagogical clarity, completeness, and alignment with the learning objectives.

5. **Refinement**
   Improves the generated content by addressing quality issues, missing information, or weaknesses identified during the review stage.

---

## 📊 Customizable Study Settings

Users can personalize their study pack using:

* 🎓 **Education Level**

  * Beginner
  * Intermediate
  * Advanced

* ⏱️ **Study Duration**

  * 30 Minutes
  * 1 Hour
  * 1 Week
  * 2 Weeks
  * 1 Month

* 🎯 **Learning Goal**

  * Define a custom learning objective or study purpose.

For example:

> Build a strong foundation in Python and prepare for practical programming projects.

---

## 🧩 Study Pack Sections

The application allows users to select the sections they need.

### 📌 Study Plan

Includes:

* Learning objectives
* Recommended topics
* Time allocation
* Difficulty level
* Study strategy

### 📖 Study Notes

Provides:

* Detailed explanations
* Important concepts
* Key points
* Examples
* Core terminology

### 🎴 Flashcards

Generates structured:

* Terms
* Definitions
* Important concepts
* Quick-review information

### 📝 Assessment & Quiz

Generates customizable MCQs based on the generated study material.

Users can select between:

**1–20 questions**

Each question includes an answer key for review.

### 💡 Exam Tips

Provides:

* Important concepts to remember
* Quick revision points
* Exam-focused strategies
* Key takeaways

---

## ⚡ Real-Time Workflow Progress

The application provides a visual progress indicator while the AI workflow is running.

Users can see the progress through:

```text
Planning
   ↓
Content Generation
   ↓
Assessment
   ↓
Quality Review
   ↓
Refinement
   ↓
Final Study Pack
```

This makes the multi-stage AI process easier to understand and provides feedback while content is being generated.

---

## 🛡️ Error Handling & Retry System

The application includes retry handling for temporary API failures and service availability issues.

It uses **exponential backoff** to retry requests when appropriate, helping reduce failures caused by temporary issues such as:

* HTTP 429 — Rate Limit
* HTTP 503 — Service Unavailable
* Temporary API/server failures

This improves the overall reliability of the application.

---

# 🧠 How the AI Workflow Works

The application follows a sequential AI orchestration architecture.

```text
┌──────────────────────────────────────┐
│          User Configuration           │
│ Topic • Level • Duration • Goal       │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│        Stage 1: Planning              │
│ Objectives • Topics • Strategy        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│     Stage 2: Content Generation      │
│ Notes • Concepts • Terms • Examples  │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│        Stage 3: Assessment            │
│ MCQs • Questions • Verification      │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│        Stage 4: Quality Review        │
│ Accuracy • Clarity • Completeness    │
└──────────────────┬───────────────────┘
                   │
                   ▼
              ┌───────────────┐
              │ Quality Check │
              └───────┬───────┘
                      │
             ┌────────┴────────┐
             │                 │
            PASS              FAIL
             │                 │
             ▼                 ▼
      ┌─────────────┐   ┌──────────────────┐
      │ Final Output│   │ Stage 5:         │
      │             │   │ Refinement       │
      └─────────────┘   │ Fix & Improve    │
                        └────────┬─────────┘
                                 │
                                 ▼
                         ┌─────────────┐
                         │ Final Output│
                         └─────────────┘
```

### 🔄 Context Passing

Information generated in earlier stages is passed to subsequent stages.

For example:

```text
User Input
    ↓
Planning
    ↓
Learning Objectives
    ↓
Content Generation
    ↓
Study Notes
    ↓
Assessment
    ↓
Quality Review
    ↓
Refinement
    ↓
Final Study Pack
```

This allows the later stages to work with the context produced by earlier stages instead of generating completely independent responses.

---

# 🛠️ Tech Stack

| Technology                   | Purpose                             |
| ---------------------------- | ----------------------------------- |
| 🐍 Python                    | Core application logic              |
| 🎈 Streamlit                 | Web interface and application state |
| ⚡ Groq                       | LLM inference                       |
| 🤖 Google Gemini             | Alternative LLM provider            |
| 📦 Groq / Google GenAI SDK   | API communication                   |
| 📋 JSON                      | Structured AI responses             |
| 🔄 Retry Logic               | API failure recovery                |
| ☁️ Streamlit Community Cloud | Application deployment              |

---

# 📁 Project Structure

```text
ai-study-pack-generator/
│
├── app.py
│   └── Streamlit UI, user inputs, controls, and result rendering
│
├── workflow.py
│   └── Multi-stage AI workflow orchestration
│
├── prompts.py
│   └── Prompts for all five AI workflow stages
│
├── ai_utils.py
│   └── AI client configuration and retry handling
│
├── requirements.txt
│   └── Python dependencies
│
├── README.md
│   └── Project documentation
│
└── .gitignore
    └── Prevents secrets, cache files, and virtual environments
```

---

# ⚙️ Local Installation

Follow these steps to run the project locally.

## 1. Clone the Repository

```bash
git clone https://github.com/MinhaRiaz/ai-study-pack-generator.git
cd ai-study-pack-generator
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Key Configuration

The application requires an API key for the configured AI provider.

For local development, create a `.streamlit` folder inside the project directory:

```text
ai-study-pack-generator/
└── .streamlit/
    └── secrets.toml
```

Add your API key to `secrets.toml`.

### Groq

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### Google Gemini

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
```

> ⚠️ **Security:** Never commit your `secrets.toml` file or API keys to GitHub.

Make sure your `.gitignore` contains:

```text
.streamlit/secrets.toml
```

---

# ▶️ Run the Application

After configuring your API key, run:

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

# 📤 How to Use

### Step 1 — Configure Your Study

Enter:

* Study topic
* Education level
* Available study duration
* Learning goal

### Step 2 — Select Study Pack Sections

Choose the sections you want:

* 📌 Study Plan
* 📖 Study Notes
* 🎴 Flashcards
* 📝 Assessment & Quiz
* 💡 Exam Tips

### Step 3 — Select Number of Questions

Use the quiz slider to select between:

```text
1–20 MCQs
```

### Step 4 — Generate the Study Pack

Click:

**🧪 Generate Study Pack**

### Step 5 — Review Your Results

The application runs the five AI workflow stages and displays the generated study material.

---

# 💡 Example Prompts / Topics to Try

You can try topics such as:

### Example 1 — Python

```text
Topic: Python Programming
Level: Beginner
Duration: 1 Week
Goal: Learn Python fundamentals and prepare for basic programming projects.
```

### Example 2 — Machine Learning

```text
Topic: Machine Learning Fundamentals
Level: Intermediate
Duration: 2 Weeks
Goal: Understand the basic concepts of machine learning and prepare for practical projects.
```

### Example 3 — Database Systems

```text
Topic: SQL and Database Management
Level: Beginner
Duration: 1 Week
Goal: Learn SQL queries, database concepts, and practice working with relational databases.
```

### Example 4 — Artificial Intelligence

```text
Topic: Generative AI
Level: Intermediate
Duration: 1 Month
Goal: Understand generative AI concepts and learn how to build AI-powered applications.
```

### Example 5 — Computer Science Exam Preparation

```text
Topic: Data Structures and Algorithms
Level: Intermediate
Duration: 1 Week
Goal: Prepare for my university exam with important concepts, revision notes, and MCQs.
```

---

# 🔒 Privacy & Security

The application sends relevant user-provided study information to the configured AI API provider for content generation.

### Security practices

* API keys are stored using **Streamlit Secrets**.
* API keys are not hardcoded in the source code.
* `.streamlit/secrets.toml` should not be committed to GitHub.
* Users should avoid entering confidential, private, or sensitive information into study prompts.

---

# ☁️ Deployment on Streamlit Community Cloud

The application can be deployed using **Streamlit Community Cloud**.

## 1. Push the Project to GitHub

Make sure your repository contains:

```text
app.py
workflow.py
prompts.py
ai_utils.py
requirements.txt
README.md
.gitignore
```

Repository:

**https://github.com/MinhaRiaz/ai-study-pack-generator**

## 2. Open Streamlit Community Cloud

Go to:

**https://share.streamlit.io/**

Sign in using your GitHub account.

## 3. Create a New App

Select:

```text
Repository:
MinhaRiaz/ai-study-pack-generator

Branch:
main

Main file:
app.py
```

## 4. Configure Secrets

Open the application's **Settings → Secrets** section and add your API key.

For example:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

Save the configuration and deploy the application.

---

# 🚀 Live Application

Try the deployed application:

### 👉 https://ai-study-pack-generator-app.streamlit.app/

---

# 🔮 Future Improvements

The project can be extended with additional features such as:

* 📄 **PDF Export** — Download complete study packs as PDFs.
* 📝 **Markdown Export** — Export generated content as Markdown.
* 🎴 **Interactive Flashcards** — Add card-flipping interactions.
* 🔊 **Audio Summaries** — Convert study notes into audio.
* 📊 **Quiz Performance Analytics** — Track quiz scores and identify weak topics.
* 🧠 **Adaptive Learning** — Automatically adjust difficulty based on quiz performance.
* 💾 **Study History** — Save previously generated study packs.
* 👤 **User Profiles** — Store personalized learning preferences.
* 🌐 **Multiple Languages** — Generate study material in different languages.
* 📈 **Learning Progress Dashboard** — Track progress over time.

---

# 🤝 Contributing

Contributions are welcome.

## 1. Fork the Repository

Create your own fork of the project on GitHub.

## 2. Clone the Repository

```bash
git clone https://github.com/MinhaRiaz/ai-study-pack-generator.git
cd ai-study-pack-generator
```

## 3. Create a Feature Branch

```bash
git checkout -b feature/new-feature
```

## 4. Make Your Changes

Implement your feature or improvement.

## 5. Commit Your Changes

```bash
git add .
git commit -m "Add new feature"
```

## 6. Push Your Branch

```bash
git push origin feature/new-feature
```

## 7. Open a Pull Request

Create a Pull Request on GitHub describing your changes.

---

# 📜 License

This project is created for **educational, portfolio, and demonstration purposes** and is released under the **MIT License**.

---

# 👩‍💻 Author

**Minha Bibi**

Computer Science Student | AI & Software Development

GitHub: **[@MinhaRiaz](https://github.com/MinhaRiaz)**

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

Your support helps encourage further development and improvements.
