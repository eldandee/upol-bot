from typing import List


class Config:
    token: str = ''
    prefix: str = '!'
    welcome_channel: int = 735899091371819032
    student_role: str = 'Student'

    cogs: List[str] = ['help', 'admin', 'calendar', 'weather']

    weather_token = '65b5078cfd3c4d143c2fa40d34377ef1'
    default_city = 'Olomouc'
    openweather_api_url = 'http://api.openweathermap.org/data/2.5/weather' + \
        '?q={}&units=metric&lang=cz&appid={}'

    guild_id: int = 0
