from pydantic import BaseModel, EmailStr, model_validator


class LoginCredentialsSchema(BaseModel):
    email: EmailStr
    password: str


class ResponseJWTTokensSchema(BaseModel):
    access_token: str
    refresh_token: str


class RegisterCredentialsSchema(LoginCredentialsSchema):
    confirm_password: str
    username: str

    @model_validator(mode="after")
    def check_passwords_match(self):
        password = self.password
        confirm_password = self.confirm_password

        if password != confirm_password:
            raise ValueError("Passwords don't match")

        return self


class RequestUpdateTokenSchema(BaseModel):
    refresh_token: str


class ResponseUpdateTokenSchema(BaseModel):
    access_token: str
