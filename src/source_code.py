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
            data = json.load(file)
            if "question" not in data or not isinstance(data["question"], list):
                print(f"Error: File '{file_path}' does not contain a valid knowledge base structure.")
                return {"question": []}
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Starting with an empty knowledge base.")
        return {"question": []}
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON. Starting with an empty knowledge base.")
        return {"question": []}


def save_knowledge_base(file_path: str, data: Dict):
    """
    Save the knowledge base to a JSON file.
    Args:
        file_path (str): The path to the JSON file where the knowledge base will be saved.
        data (Dict): The knowledge base data to save.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
    except IOError:
        print(f"Error: Unable to save knowledge base to file '{file_path}'.")


def find_best_match(user_question: str, questions: List[str]) -> Optional[str]:
    """
    Find the closest matching question from the knowledge base.
    Args:
        user_question (str): The question input by the user.
        questions (List[str]): A list of questions from the knowledge base.
    Returns:
        Optional[str]: The closest matching question or None if no match is found.
    """
    matches = get_close_matches(user_question.lower(), [q.lower() for q in questions], n=1, cutoff=0.6)
    return matches[0] if matches else None


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
        if q["question"].lower() == question.lower():
            return q["answer"]
    return None


def chat_bot():
    """
    Main chatbot function for user interaction.
    This function handles user input, matches questions, retrieves answers,
    and allows the user to teach the chatbot new information.
    """
    knowledge_base = load_knowledge_base('knowledge_base.json')

    while True:
        user_input = input('You: ').strip()

        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break

        if not user_input:
            print("Bot: Please enter a valid question.")
            continue

        question_list = [q["question"] for q in knowledge_base["question"]]
        best_match = find_best_match(user_input, question_list)

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            if answer:
                print(f'Bot: {answer}')
            else:
                print("Bot: I found a match, but I don't have an answer for it.")
        else:
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer = input('Type the answer or "skip" to skip: ').strip()

            if new_answer.lower() != 'skip':
                knowledge_base["question"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print("Bot: Thank you for teaching me!")


if __name__ == '__main__':
    chat_bot()