# login.py


def login(username: str, password: str) -> dict:
    """사용자 로그인 처리"""
    valid_users = {"admin": "1234", "user1": "abcd"}

    if username in valid_users and valid_users[username] == password:
        return {"status": "success", "user": username}
    else:
        return {"status": "fail", "message": "Invalid credentials"}


def logout(username: str) -> dict:
    """사용자 로그아웃 처리"""
    return {"status": "success", "message": f"{username} logged out"}
