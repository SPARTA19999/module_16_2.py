from fastapi import FastAPI, Path
from typing import Optional, Annotated

app = FastAPI()

# Маршрут для главной страницы
@app.get("/")
def read_main():
    return {"message": "Главная страница"}

# Маршрут для страницы администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Маршрут для страниц пользователей с параметром user_id с валидацией
@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            description="Идентификатор пользователя",
            ge=1,  # больше или равно 1
            le=100,  # меньше или равно 100
            example=1
        )
    ]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут для страниц пользователей с параметрами username и age с валидацией
@app.get("/user/{username}/{age}")
def user_info(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            description="Имя пользователя",
            min_length=5,  # минимальная длина 5 символов
            max_length=20,  # максимальная длина 20 символов
            example="UrbanUser"
        )
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            description="Возраст пользователя",
            ge=18,  # больше или равно 18
            le=120,  # меньше или равно 120
            example=24
        )
    ]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

# Дополнительный маршрут для передачи параметров через запрос (опционально)
@app.get("/user")
def user_optional_info(username: Optional[str] = None, age: Optional[int] = None):
    if username and age:
        return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
    return {"message": "Пожалуйста, укажите имя и возраст пользователя."}
