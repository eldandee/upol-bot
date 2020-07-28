from typing import List

class Config:
    token: str = ''
    prefix: str = '!'
    welcome_channel: int = 735899091371819032
    student_role: str = 'Student'

    cogs: List[str] = ['help', 'admin', 'calendar', 'weather']

    weather_token = '65b5078cfd3c4d143c2fa40d34377ef1'
    default_city = 'Brno'
