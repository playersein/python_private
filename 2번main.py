import random


win_num = 0     # 게임 통계- 이긴 횟수 변수 설정
lose_num = 0    # 게임 통계- 진 횟수 변수 설정
tie_num = 0     # 게임 통계- 비긴 횟수 변수 설정
rsp = ['rock', 'scissors', 'paper']

while True:
    com = random.choice(rsp)    # 컴퓨터의 가위바위보 랜덤 -> 변수 초기화
    player = ''                 # player의 가위바위보 input -> 변수 초기화
    game = ''                   # 게임 재시작 혹은 종료에 대한 input -> 변수 초기화
    while True:
        player = input('가위바위보를 입력하세요:')
        player = player.lower()     # 대소문자 가리지 않게 lower 메소드 사용
        if (player == 'scissors' and com == 'paper') or (player == 'rock' and com == 'scissors') or (player == 'paper' and com == 'rock'):
            print('player win!')    # 다중 if 문을 사용한 승패 여부 판별을 못해서, player가 이길 경우
            win_num += 1            # 게임 통계- 이긴 횟수
            break
        elif (player == 'paper' and com == 'scissors') or (player == 'scissors' and com == 'rock') or (player == 'rock' and com == 'paper'):
            print('player lose..')  # player가 질 경우
            lose_num += 1           # 게임 통계- 진 횟수
            break
        elif player == com:         # 비길 경우
            print('tie')
            tie_num += 1            # 게임 통계- 비긴 횟수
            break
        else:
            # ['rock', 'scissors', 'paper'] (대소문자 제외) 유효한 input 유도
            print('유효하지 않습니다. rock, scissors, paper만 입력해주세요.')

    while True:
        game = input('게임 재시작은 r, 종료는 q 입력해주세요. ')    # 가위바위보의 재시작과 종료를 위한 input
        # r, q의 대소문자 관계없이 잘 입력되도록
        game = game.lower()
        if game == 'r':
            break                                                       # 게임 재시작
        elif game == 'q':
            print('게임을 종료합니다.')
            print(f'win: {win_num} lose: {lose_num} tie: {tie_num}')    # 게임 통계
            exit()                                                      # 게임 완전히 종료
        else:
            print('다시 입력해주세요.')                                  # 해당 while문 동작
