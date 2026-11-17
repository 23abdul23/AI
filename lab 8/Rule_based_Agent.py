
import re

knowledge = {
    r"5\s*\+\s*3": "8",
    r"2\s*\+\s*2": "4",
    r"capital of india": "New Delhi",
    r"opposite of hot": "Cold"
}

def solve(question):
    for pattern, answer in knowledge.items():
        if re.search(pattern, question, re.IGNORECASE):
            return answer
    return "I don't know the answer."

print("Computer: Hello! What is your name?")
name = input("You: ")

print("Computer: Nice to meet you,", name)
print("Computer: Ask me a puzzle.")

puzzle = input("You: ")
answer = solve(puzzle)

print("Computer:", answer)
