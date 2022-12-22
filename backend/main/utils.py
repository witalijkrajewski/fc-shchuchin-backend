from datetime import datetime


def count_player_age(birthday) -> int:
    splitted_birthday = birthday.split('.')
    birth_year = int(splitted_birthday[2])
    return datetime.now().year - birth_year

