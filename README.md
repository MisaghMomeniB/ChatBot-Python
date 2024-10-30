# ChatBot Python 🐍
**Hello, I Hope You Are Well
You Are Here to Give the Necessary Training and Tips So That You Can Create a Simple Chatbot Based on Your Data.**

# Things We Want to Check Together 😉
- [What is a ChatBot?]([what-is-a-chatbot?](https://github.com/MisaghMomeniB/ChatBot-Python?tab=readme-ov-file#what-is-a-chatbot))
- [What Are the Prerequisites?](what-are-the-prerequisites?)
- [Will It Be Expandable?](will-it-be-expandable?)
- [Line by Line Code Analysis](line-by-line-code-analysis)
- [Are There Going to Be New Updates?](Are-There-Going-to-Be-New-Updates?)

# What is a ChatBot?
A Chatbot is a Software Application That Interacts With Users Through Messaging or Voice, Responding to Questions, Requests, and Conversations. Chatbots Are Used Across Various Platforms, Such as Websites, Apps, and Messaging Platforms Like Whatsapp, Telegram, and Messenger. The Primary Goal of Chatbots is to Create an Interactive and User-friendly Experience, Often Replacing or Assisting Human Services.

Chatbots Are Generally Categorized Into Two Main Types:

Rule-based Chatbots: These Chatbots Operate Based on a Set of Predefined Rules and Scenarios, Usually Offering Limited Responses. They Are Suitable for Situations That Require Fixed and Predictable Responses, Such as Answering Frequently Asked Questions or Handling Simple Requests.

AI-based Chatbots: These Chatbots Use Machine Learning Algorithms and Natural Language Processing (Nlp) to Understand and Respond to More Complex Conversations. They Are Capable of Understanding Natural Language and Adapting to Diverse Interactions, Providing Varied and Optimized Responses. For Example, Ai-powered Chatbots Like Chatgpt Use Artificial Intelligence to Answer User Questions and Hold Natural Conversations.

Applications of Chatbots:
Customer Support: Answering User Questions and Addressing Issues 24/7.
Consulting Services: Providing Guidance and Advice in Fields Like Healthcare, Finance, and Psychology.
Sales and Marketing: Assisting Users in Finding Suitable Products or Services and Offering Special Recommendations.
Education: Responding to Student Inquiries and Guiding Them Through Academic Topics.

# What Are the Prerequisites?
You Need to Be Familiar With the Python Programming Language to Be Able to Create an Ai Chatbot Using Python's Powerful and Comprehensive Libraries. There Are Many Libraries Available for Building an Ai Chatbot, but I've Decided to Start With the Simplest Approach for Now, So That We Can Explore Other Options in the Future.

All That’s Required is a Basic Understanding of Python So That You Can Comprehend the Code. We’ll Analyze Each Line of Code Step by Step, Making This a General Tutorial.

# Will It Be Expandable?
Definitely! Every Day, by Studying Extensively About Artificial Intelligence and the Functionality of Chatbots, I Will Provide You With Better and More Interesting Versions. I Will Also Expand This Project. In the Future, I Will Work More With Different Libraries and Provide Additional Explanations.

# Line by Line Code Analysis

### Import Statements

```python
import json
from difflib import get_close_matches
from typing import Dict, List, Optional
```

1. **`import json`**: This module is used for working with JSON data. It allows for encoding (serializing) Python objects into JSON format and decoding (deserializing) JSON back into Python objects.
2. **`from difflib import get_close_matches`**: This function is used to find the closest matches to a string in a list, which is particularly useful for matching user input with predefined questions in the knowledge base.
3. **`from typing import Dict, List, Optional`**: These are type hints that provide information about the types of variables and function return types, enhancing code readability and enabling better static analysis.

### Loading the Knowledge Base

```python
def load_knowledge_base(file_path: str) -> Dict:
    """
    Load the knowledge base from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file containing the knowledge base.
    
    Returns:
        Dict: A dictionary containing the knowledge base.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)  # Load and return the JSON data as a dictionary
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Starting with an empty knowledge base.")
        return {"question": []}  # Return an empty knowledge base if the file is not found
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON. Starting with an empty knowledge base.")
        return {"question": []}  # Return an empty knowledge base if JSON is invalid
```

- **Purpose**: This function loads the knowledge base from a specified JSON file. If the file does not exist or contains invalid JSON, it initializes an empty knowledge base.
- **Parameters**: 
  - `file_path`: A string representing the file path of the JSON file.
- **Returns**: A dictionary containing the knowledge base.
- **Functionality**:
  - It uses a `try-except` block to handle potential errors:
    - **`FileNotFoundError`**: Catches the error if the file does not exist and initializes an empty knowledge base.
    - **`json.JSONDecodeError`**: Catches errors in case the JSON is invalid, also initializing an empty knowledge base.

### Saving the Knowledge Base

```python
def save_knowledge_base(file_path: str, data: Dict):
    """
    Save the knowledge base to a JSON file.

    Args:
        file_path (str): The path to the JSON file where the knowledge base will be saved.
        data (Dict): The knowledge base data to save.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)  # Write the data to the file with indentation for readability
```

- **Purpose**: This function saves the current knowledge base back to the specified JSON file.
- **Parameters**: 
  - `file_path`: A string indicating where to save the JSON file.
  - `data`: A dictionary representing the knowledge base data.
- **Functionality**:
  - The `with open(file_path, 'w')` statement opens the file in write mode.
  - `json.dump(data, file, indent=2)` writes the dictionary `data` to the file in JSON format, with an indentation of 2 spaces for better readability.

### Finding the Best Match

```python
def find_best_match(user_question: str, questions: List[str]) -> Optional[str]:
    """
    Find the closest matching question from the knowledge base.

    Args:
        user_question (str): The question input by the user.
        questions (List[str]): A list of questions from the knowledge base.

    Returns:
        Optional[str]: The closest matching question or None if no match is found.
    """
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)  # Find the closest match
    return matches[0] if matches else None  # Return the best match or None if no match is found
```

- **Purpose**: This function attempts to find the closest matching question to the user's input from a list of predefined questions in the knowledge base.
- **Parameters**:
  - `user_question`: A string containing the question asked by the user.
  - `questions`: A list of strings representing the questions stored in the knowledge base.
- **Returns**: The closest matching question or `None` if no match is found.
- **Functionality**:
  - It uses `get_close_matches` from the `difflib` module:
    - `n=1`: Specifies that only the closest match should be returned.
    - `cutoff=0.6`: Sets a similarity threshold; only matches with a similarity score of 0.6 or higher will be considered.
  - The function returns the closest match if found; otherwise, it returns `None`.

### Retrieving the Answer

```python
def get_answer_for_question(question: str, knowledge_base: Dict) -> Optional[str]:
    """
    Retrieve the answer for a given question from the knowledge base.

    Args:
        question (str): The question to search for in the knowledge base.
        knowledge_base (Dict): The knowledge base containing questions and answers.

    Returns:
        Optional[str]: The answer corresponding to the question or None if not found.
    """
    for q in knowledge_base["question"]:
        if q["question"] == question:  # Check if the question matches
            return q["answer"]  # Return the corresponding answer
    return None  # Return None if the question is not found
```

- **Purpose**: This function retrieves the answer corresponding to a given question from the knowledge base.
- **Parameters**:
  - `question`: A string representing the question for which the answer is to be retrieved.
  - `knowledge_base`: The dictionary containing the knowledge base data.
- **Returns**: The answer if found; otherwise, `None`.
- **Functionality**:
  - It iterates through the list of questions in the knowledge base and checks if any match the input question.
  - If a match is found, it returns the corresponding answer; if no match is found after iterating through all questions, it returns `None`.

### Main Chatbot Function

```python
def chat_bot():
    """
    Main chatbot function for user interaction.

    This function handles user input, matches questions, retrieves answers,
    and allows the user to teach the chatbot new information.
    """
    knowledge_base = load_knowledge_base('knowledge_base.json')  # Load the knowledge base from the file
    
    while True:
        user_input = input('You: ')  # Prompt user for input
        
        if user_input.lower() == 'quit':  # Check if the user wants to exit
            break  # Exit the loop
        
        # Extract questions from the knowledge base for matching
        question_list = [q["question"] for q in knowledge_base["question"]]
        best_match = find_best_match(user_input, question_list)  # Find the best match for the user's question
        
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)  # Retrieve the answer
            if answer:
                print(f'Bot: {answer}')  # Output the answer to the user
            else:
                print('Bot: I found a match, but I don\'t have an answer for it.')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer = input('Type the answer or "skip" to skip: ')  # Prompt for a new answer
            
            if new_answer.lower() != 'skip':  # Check if the user wants to provide an answer
                knowledge_base["question"].append({"question": user_input, "answer": new_answer})  # Add new question and answer
                save_knowledge_base('knowledge_base.json', knowledge_base)  # Save the updated knowledge base
                print('Bot: Thank you for teaching me!')  # Acknowledge the new information
```

- **Purpose**: This is the main function of the chatbot that handles user interaction, retrieves answers from the knowledge base, and allows the user to teach the chatbot new information.
- **Functionality**:
  - **Loading Knowledge Base**: The knowledge base is loaded from a JSON file.
  - **User Interaction Loop**: A `while True` loop is used to continuously prompt the user for input:
    - If the user inputs "quit", the loop breaks, and the program ends.
    - It extracts the list of questions from the knowledge base for matching purposes.
    - The function then finds the best match for the user's input using `find_best_match`.
  - **Matching Process**:
    - If a match is found, it retrieves the corresponding answer using `get_answer_for_question` and prints it.
    - If no match is found, the chatbot prompts the user to provide an answer for the new question. If the user provides an answer (not skipping), it appends this new question-answer pair to the knowledge base and saves it back to the JSON file using `save_knowledge_base`.
    - It acknowledges the user for teaching it new information.

### Main Script Execution

``
if __name__ == '__main__':`` <br>
   `` chat_bot()  # Start the chatbot when the script is`` <br>
# Are There Going to Be New Updates?
**Definitely, This Project is Going to Be Updated and New Things Will Be Added to It**
