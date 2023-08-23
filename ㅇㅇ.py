import random

random_number = random.randint(1, 100)  # 랜덤 숫자

num_attempts = 0                        # 시도 횟수
user = ''
game = ''
# restart
# exit
# 게임 재시작, 종료를 위한 while문
while True:
    while user != random_number:        # user가 입력한 숫자와 랜덤 숫자가 같지 않음이 참일 때 반복
        num_attempts += 1               # 시도 횟수
        user = input('숫자를 입력하세요:')  # input
        user = int(user)                   # stry -> int

        if user <= 0 or user > 100 or user:
            print('1에서 100 사이 정수만 입력 가능합니다.')
        elif user < random_number:
            print('업')
        elif user > random_number:           # 조건문 -> 입력 숫0자에 대한 힌트 제공1
            print('다운')
        else:
            print(f'정답입니다! {num_attempts}회 시도했습니다.')   # 정답을 맞췄을 때, 시도 횟수 보여주기
            # print("정답입니다! %d회 시도했습니다." % num_attempts)

            game = input("게임 재시작 r(q를 입력하면 종료): ")  # 게임 재시작과 종료를 위한 input
            game = game.lower()
            if game == 'r':
                continue    # while - while 로 데려가고 싶어ㅠ
            elif game == 'q':
                print('게임을 종료합니다.')
                break   # 게임 종료됨. 완.
            else:
                print('잘못 입력됐습니다.게임 재시작 r, 종료 q 입력 )')
                continue

        #
