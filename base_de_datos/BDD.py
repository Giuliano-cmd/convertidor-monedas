from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String
from sqlalchemy import inspect
from sqlalchemy import select
from datetime import date
import os

#Crear tablas
_dir = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f"sqlite:///{_dir}/pruebas.db", echo=True)

class Base(DeclarativeBase):
    pass

class Cotizacion(Base):
    __tablename__ = "cotizaciones"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    monto: Mapped[float]
    fecha: Mapped[str]

def crearBDD():
    Base.metadata.create_all(engine)

def agregarCotizacion(m, f):
    Session = sessionmaker(engine)
    #print(type(f))
    with Session() as session:
        cotizacionNueva = Cotizacion(monto=m, fecha=f)

        session.add(cotizacionNueva)
        session.commit()

def borrarCotizacion(idBorrar):
    Session = sessionmaker(engine)
    with Session() as session:
        borrarCotizacion = session.scalar(select(Cotizacion).where(Cotizacion.id == idBorrar))
        
        session.delete(borrarCotizacion)
        session.commit()

def verCotizaciones():
    Session = sessionmaker(engine)
    
    with Session() as session:
        resultadoCotizaciones = session.scalars(select(Cotizacion)).all()
        return resultadoCotizaciones