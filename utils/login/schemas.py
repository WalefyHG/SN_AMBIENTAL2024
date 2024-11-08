from ninja import Schema

class LoginSchema(Schema):
    email: str
    senha: str
    