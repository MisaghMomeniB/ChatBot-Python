import json
from difflib import get_close_matches
from typing import Dict, List, Optional

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
    
def save_knowledge_base(file_path: str, data: Dict):
    """
    Save the knowledge base to a JSON file.

    Args:
        file_path (str): The path to the JSON file where the knowledge base will be saved.
        data (Dict): The knowledge base data to save.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)  # Write the data to the file with indentation for readability
        
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