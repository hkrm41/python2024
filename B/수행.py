exercise_calories = {
    "걷기": 240,
    "조깅": 400,
    "수영": 600,
    "자전거타기": 450,
    "골프": 300,
    "축구": 700,
    "배드민턴": 500,
    "농구": 500,
    "줄넘기": 700,
}

def calculate_calories_burned(exercise, duration, weight):
    """
    운동으로 소모된 칼로리를 계산하는 함수
    :param exercise: 운동 종류
    :param duration: 운동 시간(분)
    :param weight: 사용자의 몸무게(kg)
    :return: 소모된 칼로리
    """
    if exercise in exercise_calories:
        calories_per_hour = exercise_calories[exercise]
        calories_burned = calories_per_hour * (duration / 60) * (weight / 70)  
        return calories_burned
    else:
        return "이 운동은 칼로리 소모량을 계산할 수 없습니다."

def save_to_file(exercise, calories_burned):
    """
    운동과 소모된 칼로리를 파일에 저장하는 함수
    :param exercise: 운동 종류
    :param calories_burned: 운동으로 소모된 칼로리
    """
    with open("exercise_log.txt", "a", encoding='utf-8') as file:
        file.write("운동: {}\n".format(exercise))
        file.write("칼로리 소모량: {:.2f}kcal\n".format(calories_burned))
        file.write("\n")

def main():
    print("운동 종류를 선택하세요:")
    for exercise in exercise_calories:
        print("- " + exercise)

    selected_exercise = input("운동 종류를 입력하세요: ")
    duration = float(input("운동 시간(분)을 입력하세요: "))
    weight = float(input("당신의 몸무게(kg)를 입력하세요: "))

    calories_burned = calculate_calories_burned(selected_exercise, duration, weight)
    if isinstance(calories_burned, str):
        print(calories_burned)
    else:
        print("소모된 칼로리: {:.2f}kcal".format(calories_burned))
        save_to_file(selected_exercise, calories_burned)
        print("운동 기록이 파일에 저장되었습니다.")

if __name__ == "__main__":
    main()

