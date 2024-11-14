### Importing Required Modules
```python
import json
from difflib import get_close_matches
from typing import Dict, List, Optional
```
- `json`: Used to load and save the knowledge base in JSON format.
- `difflib.get_close_matches`: Helps find the closest matching question to the user’s input.
- `typing`: Provides type hints like `Dict`, `List`, and `Optional` for clearer function definitions.

### Loading the Knowledge Base
```python
def load_knowledge_base(file_path: str) -> Dict:
```
- This function loads the knowledge base from a JSON file. It takes `file_path`, a string representing the file’s location, and returns a dictionary.

```python
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
```
- Opens the specified file in read mode and loads its contents as a dictionary.

```python
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Starting with an empty knowledge base.")
        return {"question": []}
```
- If the file is not found, an error message is shown, and an empty knowledge base (dictionary with an empty `question` list) is returned.

```python
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON. Starting with an empty knowledge base.")
        return {"question": []}
```
- If the JSON file is invalid, another error message is shown, and an empty knowledge base is returned.

### Saving the Knowledge Base
```python
def save_knowledge_base(file_path: str, data: Dict):
```
- This function saves the knowledge base to a JSON file, accepting the file path and the data to save.

```python
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
```
- Opens the specified file in write mode and saves the data in JSON format with indentation for readability.

### Finding the Best Match for a User Question
```python
def find_best_match(user_question: str, questions: List[str]) -> Optional[str]:
```
- This function searches for the best matching question from the knowledge base, using `user_question` as input and `questions`, a list of known questions, as potential matches. It returns the closest match or `None` if no close match is found.

```python
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None
```
- `get_close_matches` returns a list of matches with a minimum similarity ratio of 0.6. If a match is found, it returns the first match; otherwise, it returns `None`.

### Retrieving the Answer for a Question
```python
def get_answer_for_question(question: str, knowledge_base: Dict) -> Optional[str]:
```
- This function takes a `question` and searches for it in the `knowledge_base` dictionary to retrieve its answer.

```python
    for q in knowledge_base["question"]:
        if q["question"] == question:
            return q["answer"]
    return None
```
- Iterates over each question-answer pair in the knowledge base and returns the answer if the question matches. If no match is found, it returns `None`.

### Main Chatbot Function
```python
def chat_bot():
```
- This function manages user interaction and handles input, matching, answering, and teaching new information.

```python
    knowledge_base = load_knowledge_base('knowledge_base.json')
```
- Loads the knowledge base from the file `knowledge_base.json`.

#### Main Chat Loop
```python
    while True:
        user_input = input('You: ')
```
- Prompts the user to enter a question.

```python
        if user_input.lower() == 'quit':
            break
```
- Exits the loop if the user types `quit`.

#### Matching User Input to Known Questions
```python
        question_list = [q["question"] for q in knowledge_base["question"]]
        best_match = find_best_match(user_input, question_list)
```
- Extracts questions from the knowledge base and searches for the best match to the user’s input.

#### Providing an Answer
```python
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            if answer:
                print(f'Bot: {answer}')
            else:
                print('Bot: I found a match, but I don\'t have an answer for it.')
```
- If a match is found, the function retrieves and prints the answer. If the answer is missing, a message is shown.

#### Learning a New Answer
```python
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer = input('Type the answer or "skip" to skip: ')
```
- If no match is found, the chatbot prompts the user to provide an answer or skip.

```python
            if new_answer.lower() != 'skip':
                knowledge_base["question"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you for teaching me!')
```
- If the user provides a new answer, the chatbot adds it to the knowledge base and saves it to the file, then thanks the user.

### Running the Chatbot
```python
if __name__ == '__main__':
    chat_bot()
```
- When the script is run, the `chat_bot()` function starts the chatbot application.
