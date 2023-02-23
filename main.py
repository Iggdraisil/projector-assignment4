import os
from random import randint
from time import sleep

import requests

measurement_id = "G-HVQRZ387M4"
api_secret = "v3J_c98fTAiOJjd5GTILVQ"


def mock_course_variation(course):
    variation = randint(0, 10) * 0.01
    if course >= 50:
        return course - variation
    elif course <= 30:
        return course + variation
    else:
        return course + variation - 0.05


def run():
    current_course = 40
    while True:
        current_course = mock_course_variation(current_course)
        result = requests.post(
            url=f"https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}&api_secret={api_secret}",
            json={
                "client_id": "1897883207.1677192484",
                "events": [
                    {
                        "name": "USD_UAH",
                        "params": {
                            "currency_course": current_course,
                            "session_id": "123"
                        },
                    },
                ],
            },
        )
        print('metric')
        sleep(randint(5, 10))


if __name__ == "__main__":
    run()
