import random

# random_number = random.randint(1, 100)
max_num_attempts = 0
# num_attempts = 0
# user = ''
# game = ''
# restart
# exit
# 게임 재시작, 종료를 위한 while문
while True:
    random_number = random.randint(1, 100)  # 랜덤 숫자
    num_attempts = 0                        # 시도 횟수
    game = ''                               # input 하는 변수 game -> 초기화
    user = ''                               # input 하는 변수 user -> 초기화

    while user != random_number:            # user가 입력한 숫자와 랜덤 숫자가 같지 않음이 참일 때 반복
        num_attempts += 1                   # 시도 횟수
        user = input('숫자를 입력하세요:')   # input
        user = int(user)                    # str -> int

        if user <= 0 or user > 100:
            print('1에서 100 사이 정수만 입력 가능합니다.')
        elif user < random_number:                          # 입력 숫자에 대한 힌트 제공1
            print('업')
        elif user > random_number:
            print('다운')
        else:
            print(f'정답입니다! {num_attempts}회 시도했습니다.')   # 정답을 맞추면, 시도한 횟수 보여주기
            # print("정답입니다! %d회 시도했습니다." % num_attempts)

    while True:

        # 게임 재시작과 종료를 위한 input
        game = input("게임 재시작을 원하면 r, 종료를 원하면 q 를 입력해주세요. ")
        # r, q 대문자 소문자 모두 적용되도록
        game = game.lower()
        if game == 'r':
            print('게임을 다시 시작합니다.')
            if num_attempts >= max_num_attempts:            # if 문을 이용해 최고 시도횟수 저장
                max_num_attempts = num_attempts
            # r을 누르면, 이 while문에서 break해서, 큰 while문의 처음으로 돌아감
            break

        elif game == 'q':
            print('게임을 종료합니다.')
            # 게임 종료시, 최고 시도 횟수 보여주기
            print(f'최고 시도 횟수는 {max_num_attempts}회입니다.')
            exit()                                                  # 완전히 종료하기(내장 함수 이용해서)

        else:
            # r 또는 q가 아닌 다른 것을 입력했을 시에 다시 입력하도록 유도
            print('잘못 입력됐습니다.')
