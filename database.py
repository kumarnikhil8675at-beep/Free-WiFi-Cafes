from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped,relationship
from sqlalchemy import Integer, String , Boolean
from flask_login import UserMixin

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)


class cafe(db.Model):
    __tablename__="cafe"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String, nullable=True)
    map_url:Mapped[str] = mapped_column(String, nullable=True)
    img_url:Mapped[str] = mapped_column(String, nullable=True)
    location:Mapped[str] = mapped_column(String, nullable=True)
    has_sockets:Mapped[bool] = mapped_column(Boolean, nullable=True)
    has_toilet:Mapped[bool] = mapped_column(Boolean, nullable=True)
    has_wifi:Mapped[bool] = mapped_column(Boolean, nullable=True)
    can_take_calls:Mapped[bool] = mapped_column(Boolean, nullable=True)
    seats:Mapped[str] = mapped_column(String, nullable=True)
    coffee_price:Mapped[str] = mapped_column(String, nullable=True)
    #chnges
    user_id:Mapped[int]= mapped_column(Integer,db.ForeignKey("User.id"))
    
    rating_id = relationship("rating",back_populates="cafe")
    m_user = relationship("User",back_populates="cafe_id")

class User(UserMixin,db.Model):
    __tablename__="User"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    Name:Mapped[str] = mapped_column(String, nullable=False,unique=True)
    Password:Mapped[str] = mapped_column(String, nullable=False)
    
    rating_check = relationship("rating",back_populates="user")
    cafe_id = relationship("cafe",back_populates="m_user")
    

class rating(db.Model):
    __tablename__="rating"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    ratting:Mapped[int]=mapped_column(Integer,nullable=True)
    
    who_rate:Mapped[int]=mapped_column(Integer,db.ForeignKey("User.id"))
    who_cafe:Mapped[int]=mapped_column(Integer,db.ForeignKey("cafe.id"))
    
    user = relationship("User",back_populates="rating_check")
    cafe = relationship("cafe",back_populates="rating_id")