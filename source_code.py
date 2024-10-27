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