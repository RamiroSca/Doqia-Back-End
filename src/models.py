from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float, Date, Enum,JSON
from sqlalchemy.orm import relationship
from datetime import datetime
# from . import db


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    is_client = Column(Boolean, default=True)
    sexo = Column(String(10), nullable=True)
    altura = Column(Float, nullable=True)
    nombre = Column(String(80))
    peso = Column(Float, nullable=True)
    edad = Column(Integer, nullable=True)
    fecha_de_nacimiento = Column(Date, nullable=True)
    alergias_alimentarias = Column(String(255), nullable=True)
    medicamentos_actuales = Column(String(255), nullable=True)
    vacunas = Column(String(255), nullable=True)
    historial_familiar = Column(String(255), nullable=True)
    numero_salud = Column(String(50), nullable=True)
    image_url = Column(String(255), nullable=True)
    ciudad = Column(String(50), nullable=True)
    available_times = Column(JSON, nullable=True)  # Nuevo campo para horarios disponibles
    # reservations = relationship('Reservation', backref='client', lazy=True)
    # services = relationship('Service', backref='user', lazy=True)
    # accepted_reservations = relationship('Reservation', primaryjoin="and_(User.id==Reservation.client_id, Reservation.accept==True)", lazy=True)

class UserImage(db.Model):
    __tablename__ = 'user_image'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    image_url = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    upload_date = Column(String(50), nullable=True)
    
class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    # occupations = db.Column(db.JSON, nullable=False, default=[])  # Cambiado a lista vacía
    # type = db.Column(db.Enum('telemedicina', 'domicilio', 'ambos'), nullable=False)
    # prices = db.Column(db.JSON, nullable=True, default={})  # Agregar este campo
    # reservations = db.relationship('Reservation', backref='service', lazy=True)


class Comment(db.Model):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    # service_id = Column(Integer, ForeignKey('service.id'), nullable=False)
    text = Column(String(255), nullable=False)
    # service = relationship('Service', backref=db.backref('comments', lazy=True))

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    # reservation_date = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    # patient_name = db.Column(db.String(100), nullable=False)
    # address = db.Column(db.String(200), nullable=False)
    # time_slot = db.Column(db.String(50), nullable=False)
    # comment = db.Column(db.String(500))
    # accept = db.Column(db.Boolean, default=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            # 'client_id': self.client_id,
            # 'service_id': self.service_id,
            # 'reservation_date': self.reservation_date.isoformat(),
            'type': self.type,
            # 'patient_name': self.patient_name,
            # 'address': self.address,
            # 'time_slot': self.time_slot,
            # 'comment': self.comment,
            # 'accept': self.accept
        }

class SavedService(db.Model):
    __tablename__ = 'saved_service'
    id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # service_id = Column(Integer, ForeignKey('service.id'), nullable=False)
    # saved_date = Column(DateTime, default=datetime.utcnow)

    # user = relationship('User', backref='saved_services', lazy=True)
    # service = relationship('Service', backref='saved_by_users', lazy=True)

class Familiar(db.Model):
    __tablename__ = 'familiar'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    parentesco = Column(String(50), nullable=False)
    # user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # user = relationship('User', backref='familiares')

    def __repr__(self):
        return f'<Familiar(nombre={self.nombre}, parentesco={self.parentesco})>'