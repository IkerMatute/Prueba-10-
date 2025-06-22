# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    libros = relationship("Libro", back_populates="autor")

    def __repr__(self):
        return f"<Autor(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}')>"

class Genero(Base):
    __tablename__ = 'generos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    libros = relationship("Libro", back_populates="genero")

    def __repr__(self):
        return f"<Genero(id={self.id}, nombre='{self.nombre}')>"

class Libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    fecha_publicacion = Column(Date, default=datetime.date.today)
    autor_id = Column(Integer, ForeignKey('autores.id'))
    genero_id = Column(Integer, ForeignKey('generos.id'))

    autor = relationship("Autor", back_populates="libros")
    genero = relationship("Genero", back_populates="libros")

    def __repr__(self):
        return f"<Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor.nombre if self.autor else 'N/A'}', genero='{self.genero.nombre if self.genero else 'N/A'}')>"

# Configuración de la base de datos
DATABASE_URL = "sqlite:///biblioteca.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
    print("Base de datos inicializada.")

if __name__ == '__main__':
    init_db()