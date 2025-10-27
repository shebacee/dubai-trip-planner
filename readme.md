 <h1>Dubai Trip Assistant Chatbot</h1>
   An intelligent AI-powered conversational chatbot designed to help users plan their perfect Dubai vacation. Built with Python, Streamlit, and OpenAI's GPT-4o-mini API.

##  Features

- **Personalized Travel Recommendations**: Tailored suggestions for accommodations, dining, transportation, and sightseeing based on user preferences and budget
- **Interactive Chat Interface**: Real-time conversational experience powered by Streamlit
- **Session Management**: Maintains conversation context and chat history throughout user interactions
- **Professional AI Persona**: Custom-designed "JV" assistant that provides concise, expert guidance (responses under 200 words)
- **Secure API Integration**: Environment variable configuration for safe API key management

##  Tech Stack

- **Python**: Core programming language
- **Streamlit**: Frontend framework for interactive web interface
- **OpenAI API (GPT-4o-mini)**: Natural language processing and response generation
- **python-dotenv**: Environment variable management

##  Prerequisites

- Python 3.7 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- pip package manager

##  Installation & Setup

1. **Clone the repository**
```bash
   git clone https://github.com/YOUR_USERNAME/dubai-trip-planner.git
   cd dubai-trip-planner
```

2. **Create a virtual environment** (recommended)
```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
```
   OPENAI_API_KEY=your_api_key_here
```

5. **Run the application**
```bash
   streamlit run chatbot.py
```

6. **Access the chatbot**
   
   Open your browser and navigate to `http://localhost:8501`

##  Dependencies
```
openai
streamlit
python-dotenv
```

##  Usage

1. Launch the application using the command above
2. Start chatting with JV, your Dubai trip planning expert
3. Provide details about your:
   - Travel dates
   - Budget
   - Interests and preferences
   - Group size
4. Receive personalized recommendations and itinerary suggestions

##  Security Note

Never commit your `.env` file or expose your API keys. The `.gitignore` file is configured to prevent accidental exposure.

##  Project Structure
```
dubai-trip-planner/
├── chatbot.py          # Main application file
├── .env                # Environment variables (not tracked)
├── .gitignore          # Git ignore rules
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

##  Future Enhancements

- Add multi-language support
- Integrate real-time pricing and booking APIs
- Include weather forecast integration
- Add interactive maps and visual itineraries
- Implement user feedback and rating system

##  Author

Sheba
- GitHub: https://github.com/shebacee
- LinkedIn: www.linkedin.com/in/fathimath-sheba-c

##  License

This project is open source and available under the [MIT License](LICENSE).

##  Acknowledgments

- OpenAI for providing the GPT-4o-mini API
- Streamlit for the intuitive web framework
- The Python community for excellent libraries and tools

---

⭐ If you find this project helpful, please consider giving it a star!
