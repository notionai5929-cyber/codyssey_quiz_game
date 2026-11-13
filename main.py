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
        
        # 앞뒤 공백 제거 처리
        choice = input("선택: ").strip()

        # 빈 입력 처리
        if not choice:
            print("⚠️ 빈 입력입니다. 1~5 사이의 숫자를 입력해주세요.")
            continue

        # 메뉴 번호별 흐름 제어 및 예외 처리
        if choice == '1':
            print("📝 퀴즈 풀기를 시작합니다.")
            # 기능 구현 예정
        elif choice == '2':
            print("📌 새로운 퀴즈를 추가합니다.")
            # 기능 구현 예정
        elif choice == '3':
            print("📋 등록된 퀴즈 목록을 출력합니다.")
            # 기능 구현 예정
        elif choice == '4':
            print("🏆 최고 점수를 확인합니다.")
            # 기능 구현 예정
        elif choice == '5':
            print("게임을 종료합니다.")
            break
        else:
            print("⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C 나 EOF 발생 시 강제 종료를 막고 안전하게 처리
        print("\n프로그램을 안전하게 종료합니다.")