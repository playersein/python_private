import random

random_number = random.randint(1, 100)

num_attempts = 0
user = ''

while user != random_number:
    user = input('숫자를 입력하세요:')
    user = int(user)
    num_attempts += 1
    if user > random_number:
        print('다운')
    elif user < random_number:
        print('업')
    else:
        # print("정답입니다! %d회 시도했습니다." % num_attempts)
        print(f'정답입니다! {num_attempts}회 시도했습니다.')
