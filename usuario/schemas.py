from ninja import Schema
from typing import Optional

class UsuarioSchemaIn(Schema):
    nome: str
    email: str
    senha: str

class UsuarioSchemaOut(Schema):
    id: int
    nome: str
    email: str
    senha: str

# Schema para tratar a atualização de usuario 
class UsuarioSchemaPut(Schema):
    nome: Optional[str] = ''
    email: Optional[str] = ''
    senha: Optional[str] = ''