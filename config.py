import os
from dotenv import load_dotenv
class Config:
    load_dotenv()
    token: str = os.getenv('DISCORD_TOKEN')
    prefix: str = '!'
    welcome_channel: int = 735899091371819032
    student_role: str = 'Student'

    cogs = ['help', 'admin', 'calendar', 'weather','autopin','name_day']

    weather_token = '65b5078cfd3c4d143c2fa40d34377ef1'
    default_city = 'Olomouc'
    openweather_api_url = 'http://api.openweathermap.org/data/2.5/weather' + \
        '?q={}&units=metric&lang=cz&appid={}'

    guild_id: int = 0

     # Pin emoji count to pin
    pin_count: int = 5
    pin_banned_channels = [734420885724856431,734420846172438588,734419921491984474,734420918079848449,734421004021137468]
