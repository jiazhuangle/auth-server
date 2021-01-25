from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey,DATETIME,Table,Enum as SQL_ENum
from sqlalchemy.orm import relationship,backref

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(64), index=True)
    email = Column(String(128), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    department_id = Column(Integer, ForeignKey("department.id"))
    department = relationship('Department', backref="users")


class Department(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), index=True)
    description = Column(String(256), index=True)


project_user = Table('project_user',Base.metadata,
                   Column('user_id',  Integer,  ForeignKey('user.id'), primary_key=True),
                   Column('project_id', Integer, ForeignKey('project.id'), primary_key=True))


class Project(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), index=True)
    description = Column(String(256), index=True)
    #'not begin ongoing suspand finish
    status = Column(String(16))
    create_date = Column(DATETIME,default=datetime.now)

    users = relationship('User', secondary=project_user, backref=backref('projects'))

