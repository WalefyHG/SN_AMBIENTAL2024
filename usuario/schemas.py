from ninja import Schema

class UsuarioSchemaIn(Schema):
    nome: str
    email: str
    senha: str

class UsuarioSchemaOut(Schema):
    id: int
    nome: str
    email: str
    senha: str