# quiz.py

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 사이의 정수 정답 번호

    def display(self):
        print(f"\nQ. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        return self.answer == user_answer
    
    def get_default_quizzes():
        return [
            Quiz("Python의 창시자는?", ["Guido", "Linus", "Bjarne", "James"], 1),
            Quiz("다음 중 파이썬의 기본 자료형이 아닌 것은?", ["int", "str", "float", "array"], 4),
            Quiz("파이썬에서 리스트의 길이를 구하는 함수는?", ["size()", "length()", "len()", "count()"], 3),
            Quiz("조건문 키워드가 아닌 것은?", ["if", "elif", "else", "then"], 4),
            Quiz("클래스 내부에서 인스턴스 자신을 가리키는 키워드는?", ["this", "self", "me", "cls"], 2)
    ]