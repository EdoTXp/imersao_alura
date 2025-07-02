"""
Module documentation goes here.

This module contains SQLAlchemy models for the school management system.
It defines classes for Matricula, Aluno, and Curso.

Classes:
    Matricula: Represents a school enrollment.
    Aluno: Represents a student in the system.
    Curso: Represents a course in the school system.
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Matricula(Base):
    """
    Represents a school enrollment.

    Attributes:
        id (int): The unique identifier for the enrollment.
        aluno_id (int): The foreign key referencing the Aluno table.
        curso_id (int): The foreign key referencing the Curso table.
        aluno (Aluno): The related Aluno object.
        curso (Curso): The related Curso object.
    """
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    curso_id = Column(Integer, ForeignKey("cursos.id"))

    aluno = relationship("Aluno", back_populates="matriculas")
    curso = relationship("Curso", back_populates="matriculas")


class Aluno(Base):
    """
    Represents a student in the system.

    Attributes:
        id (int): The unique identifier for the student.
        nome (str): The student's name.
        email (str): The student's email address.
        telefone (str): The student's phone number.
    """
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

    matriculas = relationship("Matricula", back_populates="aluno")


class Curso(Base):
    """
    Represents a course in the school system.

    Attributes:
        id (int): The unique identifier for the course.
        nome (str): The name of the course.
        codigo (str): The unique code of the course.
        descricao (str): A description of the course.
    """
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    codigo = Column(String, nullable=False, unique=True)
    descricao = Column(Text)

    matriculas = relationship("Matricula", back_populates="curso")
