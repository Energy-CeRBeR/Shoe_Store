from pydantic_core._pydantic_core import PydanticCustomError
from pydantic import field_validator, validate_email, BaseModel


class LoginModel(BaseModel):
    email: str
    password: str

    @field_validator('email')
    def is_valid_email(cls, email):
        try:
            validate_email(email)
            return email
        except PydanticCustomError:
            return {'response': 'Введите валидный email'}

