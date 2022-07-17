from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'

# декоратор датакласс

@dataclass
class User:
    first_name: str = 'Dev'
    last_name: str = 'Patel'
    email: str = 'dev_patel@gmail.com'
    gender: str = 'Male'
    mobile_number: str = '9999119999'
    birthday_year: int = 1990
    birthday_month: int = 4
    birthday_month_name: str = 'April'
    birthday_day: int = 23
    subjects: Tuple[str] = 'Computer Science', 'Social Studies', 'Chemistry', 'Maths', 'Physics'
    hobbies: Tuple[str] = 'Sports', 'Reading', 'Music'
    picture: str = 'screen.png'
    address: str = 'Milky Way, Solar System, Earth'
    state: str = 'Uttar Pradesh'
    city: str = 'Agra'


class Subjects:
    computer_science = 'Computer Science'
    social_studies = 'Social Studies'
    chemistry = 'Chemistry'
    maths = 'Maths'
    physics = 'Physics'


class Hobbies:
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'




# OR
# class User:
#    foo = bar - метод класса
#     def __init__(self, first_name, last_name, subjects):
#         self.first_name = first_name - метод обьекта класса
#         self.last_name = last_name
#         self.subjects = subjects
