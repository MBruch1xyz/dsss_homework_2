import random

def random_integer(min_value, max_value):
    """
    Generates a random integer within the specified range (inclusive).

    Parameters:
    - min_value (int): The minimum value of the range.
    - max_value (int): The maximum value of the range.

    Returns:
    int: A random integer within the specified range.
    """
    return random.randint(min_value, max_value)

def random_operator():
    """
    Selects a random arithmetic operator from the set ('+', '-', '*').

    Returns:
    str: A randomly chosen operator.
    """
    return random.choice(['+', '-', '*'])

def math_operation(operand1, operand2, operator):
    """
    Performs a mathematical operation based on the provided operator.

    Parameters:
    - operand1 (int): The first operand.
    - operand2 (int): The second operand.
    - operator (str): The operator ('+', '-', '*').

    Returns:
    Tuple[str, int]: A tuple containing the mathematical problem as a string and the result of the operation.
    """
    problem = f"{operand1} {operator} {operand2}"# Create a string representing a mathematical expression using f-string
    try:
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        else:
            result = operand1 * operand2
    except Exception as e:
        print(f"Error performing the math operation: {e}")
        result = None

    return problem, result

def math_quiz():
    """
    Conducts a math quiz game where the user needs to solve random arithmetic problems.
    """
    user_score = 0  # Variable to track the user's score
    total_questions = 3  # Adjusted for better readability

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        operand1 = random_integer(1, 10)
        operand2 = random_integer(1, 5)
        operator = random_operator()

        problem, correct_answer = math_operation(operand1, operand2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            user_score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {user_score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
