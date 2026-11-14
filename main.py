# main.py
import json
import os
from quiz import Quiz

class QuizGame:
    def __init__(self, data_file="state.json"):
        self.data_file = data_file
        self.quizzes = []
        self.best_score = 0
        self.load_data()  # 게임 시작 시 데이터 불러오기

    def load_data(self):
        if not os.path.exists(self.data_file):
            self.quizzes = Quiz.get_default_quizzes()
            return

        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                quiz_list = data.get("quizzes", [])
                self.quizzes = [Quiz.from_dict(q) for q in quiz_list]
        except (json.JSONDecodeError, KeyError):
            print("⚠️ 데이터 파일이 손상되었습니다. 기본 퀴즈로 초기화합니다.")
            self.quizzes = Quiz.get_default_quizzes()
            self.best_score = 0

    def save_data(self):
        data = {
            "best_score": self.best_score,
            "quizzes": [q.to_dict() for q in self.quizzes]
        }
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def play_quiz(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0

        for i, quiz in enumerate(self.quizzes, 1):
            print("\n----------------------------------------")
            print(f"[문제 {i}]")
            quiz.display()
            
            while True:
                try:
                    user_answer = int(input("\n정답 입력 (1~4): ").strip())
                    if user_answer not in [1, 2, 3, 4]:
                        print("⚠️ 허용 범위 밖 숫자입니다. 1~4 사이의 숫자를 입력해주세요.")
                        continue
                    break
                except ValueError:
                    print("⚠️ 숫자 변환 실패. 올바른 숫자를 입력해주세요.")

            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. (정답: {quiz.answer}번)")

        print("\n========================================")
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        if score > self.best_score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = score
        print("========================================")
        self.save_data()  # 게임이 끝난 후 최고 점수 저장

    def run(self):
        while True:
            print("\n========================================")
            print("        🎯 나만의 퀴즈 게임 🎯        ")
            print("========================================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("========================================")
            
            choice = input("선택: ").strip()

            if not choice:
                print("⚠️ 빈 입력입니다. 1~5 사이의 숫자를 입력해주세요.")
                continue

            if choice == '1':
                self.play_quiz()
            elif choice == '2':
                self.add_quiz()
            elif choice == '3':
                self.show_quiz_list()
            elif choice == '4':
                print(f"🏆 최고 점수: {self.best_score}점")
            elif choice == '5':
                print("게임을 종료합니다.")
                break
            else:
                print("⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")
    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = input("문제를 입력하세요: ").strip()
        if not question:
            print("⚠️ 빈 입력입니다. 퀴즈 추가를 취소합니다.")
            return
        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            choices.append(choice)
        while True:
            try:
                answer = int(input("정답 번호 (1-4): ").strip())
                if answer not in [1, 2, 3, 4]:
                    print("⚠️ 허용 범위 밖 숫자입니다. 1~4 사이의 숫자를 입력해주세요.")
                    continue
                break
            except ValueError:
                print("⚠️ 숫자 변환 실패. 올바른 숫자를 입력해주세요.")
        # 새로운 퀴즈 객체를 생성하고 목록에 추가한 뒤 파일에 저장
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_data()
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")
    def show_quiz_list(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"[{i}] {quiz.question}")
        print("----------------------------------------")

def main():
    game = QuizGame()
    game.run()

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n프로그램을 안전하게 종료합니다.")