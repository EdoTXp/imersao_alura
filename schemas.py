"""
Module documentation goes here.

This module contains Pydantic schemas for the school management system.
It defines classes for Aluno, Curso, and Matricula.
"""
from typing import List
from pydantic import BaseModel, EmailStr


class Matricula(BaseModel):
    """
    Represents a school enrollment.

    Attributes:
        aluno_id (int): The ID of the enrolled student.
        curso_id (int): The ID of the enrolled course.
    """
    aluno_id: int
    curso_id: int

    class Config:
        """
        Configuration settings for Pydantic models.

        This class is used to configure the behavior of Pydantic models,
        such as setting default values or customizing
        serialization/deserialization.
        """
        from_attributes = True
        from_attributes = True


Matriculas = List[Matricula]


class Aluno(BaseModel):
    """
    Represents a student in the school management system.

    Attributes:
        nome (str): The student's name.
        email (EmailStr): The student's email address.
        telefone (str): The student's phone number.
    """
    nome: str
    email: EmailStr
    telefone: str

    class Config:
        """
        Configuration settings for Pydantic models.
        This class is used to configure the behavior of Pydantic models,
        such as setting default values or customizing
        serialization/deserialization.
        """
        from_attributes = True


Alunos = List[Aluno]


class Curso(BaseModel):
    """
    Represents a course in the school management system.
    Attributes:
        nome (str): The name of the course.
        codigo (str): The unique identifier of the course.
        descricao (str): A brief description of the course.
    """
    nome: str
    codigo: str
    descricao: str

    class Config:
        """
        Configuration settings for Pydantic models.
        This class is used to configure the behavior of Pydantic models,
        such as setting default values or customizing
        serialization/deserialization.
        """
        from_attributes = True


Cursos = List[Curso]
