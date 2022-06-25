from random import randint

# 무작위로 1 - 45 사이의 숫자 6개 뽑기


def generate_numbers():
    # 숫자 6개를 보관할 리스트 생성
    numbers = []

    # 6개의 요소가 있을때까지 반복
    while len(numbers) < 6:
        # 새로 뽑은 수가 numbers에 없을 경우에만 추가
        new_number = randint(1, 43)
        if new_number not in numbers:
            numbers.append(new_number)

    # 정렬하고 리턴
    return sorted(numbers)

# 보너스까지 포함해 7개 숫자 뽑기


def draw_winning_numbers():
    winning_numbers = generate_numbers()
    while len(winning_numbers) < 7:
        new_number = randint(1, 43)
        if new_number not in winning_numbers:
            winning_numbers.append(new_number)

    # 정렬하지 않고 리턴
    return winning_numbers

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기


def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        # num이 winning_numbers에 있으면 count에 1 추가
        if num in winning_numbers:
            count = count + 1

    return count

# 로또 등수 확인하기


def check(numbers, winning_numbers):
    # 번호 당첨 개수 확인
    count = count_matching_numbers(numbers, winning_numbers[:6])

    # 보너스 당첨 확인
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    # 상금 확인
    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
