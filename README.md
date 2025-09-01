Gemini Agent Example
Ye project Google Gemini API ko OpenAI-compatible interface ke through use karta hai
aur ek simple Agent banata hai jo aapke questions ka jawab deta hai.

🔧 Requirements
Python 3.9+
Virtual environment (recommended)
API key from Google AI Studio
📦 Installation
Repository clone ya code copy karein.

Virtual environment banayein aur activate karein:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Dependencies install karein:

bash Copy code pip install -r requirements.txt Agar requirements.txt nahi hai, to manually install karein:

bash Copy code pip install python-dotenv pip install agents 🔑 Environment Variables Project ke root me ek .env file banayein aur apna Gemini API key add karein:

ini Copy code GEMINI_API_KEY=your_api_key_here ▶️ Run the Script Script run karne ke liye:

bash Copy code python main.py Ye aapse input lega:

yaml Copy code Ask your question: Aur phir model ka response terminal me print karega.

🛠 Notes Agar aap AsyncOpenAI use kar rahe ho, to script ko asyncio.run() ke sath chalana padega.

Agar simple synchronous version chahiye, to AsyncOpenAI ki jagah OpenAI client use karein.

Debugging ke liye check karein ki API key sahi load ho rahi hai:

python Copy code print("API Key Loaded:", bool(gemini_api_key)) 📄 Example csharp Copy code Ask your question: What is the capital of France? 🤖 Response: Paris is the capital of France.
