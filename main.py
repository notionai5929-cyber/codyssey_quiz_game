# main.py
from quiz import get_default_quizzes

def play_quiz():
    quizzes = get_default_quizzes()
    
    if not quizzes:
        print("⚠️ 등록된 퀴즈가 없습니다.")
        return

    print(f"\n📝 퀴즈를 시작합니다! (총 {len(quizzes)}문제)")
    score = 0

    for i, quiz in enumerate(quizzes, 1):
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
    print(f"🏆 결과: {len(quizzes)}문제 중 {score}문제 정답!")
    print("========================================")

def main():
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
            play_quiz()
        elif choice == '2':
            print("📌 새로운 퀴즈를 추가합니다.")
        elif choice == '3':
            print("📋 등록된 퀴즈 목록을 출력합니다.")
        elif choice == '4':
            print("🏆 최고 점수를 확인합니다.")
        elif choice == '5':
            print("게임을 종료합니다.")
            break
        else:
            print("⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n프로그램을 안전하게 종료합니다.")