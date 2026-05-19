# IoT Sensor Dashboard - 메인 앱
# app.py

from login import login


def run():
    print("IoT Dashboard 시작")
    result = login("admin", "1234")
    print(f"로그인 결과: {result}")


if __name__ == "__main__":
    run()
