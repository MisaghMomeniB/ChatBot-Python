### 🚀 ChatBot with JSON Knowledge Base 🌟

Welcome to the **ChatBot with Dynamic Learning**! 🤖 This simple yet powerful chatbot uses a **JSON-based knowledge base** to interact with users. If the bot doesn't know an answer, you can teach it, and it will remember your input for future interactions! ✨

---

## 🔥 Features at a Glance:

1. **Dynamic Knowledge Base** 📚  
   - Stores questions and answers in a JSON file (`knowledge_base.json`).  
   - Automatically updates the knowledge base when you teach the bot something new.  

2. **Learning on the Fly** 🧠  
   - When the bot encounters a question it doesn't know, it asks for your help to learn.  

3. **Intelligent Matching** 🎯  
   - Uses fuzzy matching (`difflib.get_close_matches`) to understand your input and find the closest known question.  

4. **Persistent Memory** 💾  
   - All updates to the knowledge base are saved immediately and persist across sessions.  

5. **Easy to Use** 👌  
   - Start the chatbot, interact with it, and teach it new things—all in one script!

---

## 🌟 How It Works

1. The bot starts by loading a JSON file that contains its knowledge base.  
2. You ask it questions, and it tries to find the best match using fuzzy matching.  
3. If the bot doesn't know the answer, it asks you for help.  
4. When you provide an answer, the bot updates its knowledge base and thanks you! 🥳  

---

## 🚀 Get Started

1. **Clone the Repository** 🖥️  
   ```bash
   git clone https://github.com/your-username/chatbot.git
   cd chatbot
   ```

2. **Run the Chatbot** 🎉  
   ```bash
   python chatbot.py
   ```

3. **Interact with the Bot** 💬  
   - Ask questions, like:  
     ```
     You: Hello
     Bot: I don’t know the answer. Can you teach me?
     Type the answer or "skip" to skip: Hi there!
     Bot: Thank you for teaching me!
     ```
   - Exit the bot anytime by typing `quit`.

4. **Teach the Bot** 🧑‍🏫  
   - If the bot doesn't know an answer, you can provide one.  
   - The knowledge base will be updated dynamically and persist across sessions.  

---

## 📂 JSON Knowledge Base Structure

The bot uses a JSON file (`knowledge_base.json`) to store its knowledge. Here's an example structure:

```json
{
  "question": [
    {
      "question": "Hello",
      "answer": "Hi there!"
    },
    {
      "question": "How are you?",
      "answer": "I'm just a bot, but I'm doing great!"
    }
  ]
}
```

---

## 💡 Future Enhancements

- **Advanced Matching**:
  - Use NLP libraries like `spaCy` or `transformers` for better semantic understanding.
  
- **GUI Integration**:
  - Add a graphical user interface for easier interactions.
  
- **Database Support**:
  - Migrate to a database (like SQLite or MongoDB) for better scalability.

---

## 📜 Code Breakdown (Line by Line)

### Import Statements
```python
import json
from difflib import get_close_matches
from typing import Dict, List, Optional
```
- **`json`**: Used for reading and writing the knowledge base file.  
- **`difflib.get_close_matches`**: Finds the closest match for user input based on similarity.  
- **`typing`**: Provides type hints for better code readability.

---

### Load the Knowledge Base
```python
def load_knowledge_base(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Starting with an empty knowledge base.")
        return {"question": []}
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON. Starting with an empty knowledge base.")
        return {"question": []}
```
- Loads the JSON file containing the knowledge base.  
- Handles errors for missing or invalid files gracefully by starting with an empty knowledge base.

---

### Save the Knowledge Base
```python
def save_knowledge_base(file_path: str, data: Dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
```
- Saves the updated knowledge base to the JSON file.  
- Data is formatted with indentation for readability.

---

### Find the Best Match
```python
def find_best_match(user_question: str, questions: List[str]) -> Optional[str]:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None
```
- Finds the most similar question in the knowledge base using fuzzy matching.  
- Returns the best match if the similarity is above a threshold (`cutoff=0.6`).

---

### Get the Answer for a Question
```python
def get_answer_for_question(question: str, knowledge_base: Dict) -> Optional[str]:
    for q in knowledge_base["question"]:
        if q["question"] == question:
            return q["answer"]
    return None
```
- Searches the knowledge base for an exact match to the question.  
- Returns the corresponding answer or `None` if no match is found.

---

### Main Chatbot Function
```python
def chat_bot():
    knowledge_base = load_knowledge_base('knowledge_base.json')
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        question_list = [q["question"] for q in knowledge_base["question"]]
        best_match = find_best_match(user_input, question_list)
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            if answer:
                print(f'Bot: {answer}')
            else:
                print('Bot: I found a match, but I don\'t have an answer for it.')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer = input('Type the answer or "skip" to skip: ')
            if new_answer.lower() != 'skip':
                knowledge_base["question"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you for teaching me!')
```
- Handles the main interaction loop for the chatbot:
  - Prompts for user input.
  - Matches questions with the knowledge base.
  - Retrieves or learns answers dynamically.

---

### Running the Script
```python
if __name__ == '__main__':
    chat_bot()
```
- Ensures the chatbot function runs only when the script is executed directly.

---

Feel free to clone, use, and enhance this chatbot. Contributions are welcome! 🌟  
Let's make learning fun for the bot and you! 😊
