from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///configs.db', echo=True)
Session = sessionmaker(bind=engine)

class Config(Base):
    __tablename__ = 'configs'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    config_data = Column(JSON, nullable=False)

def init_db():
    Base.metadata.create_all(engine)

def save_config(name, config_data):
    session = Session()
    new_config = Config(name=name, config_data=config_data)
    session.add(new_config)
    session.commit()
    session.close()

def get_all_configs():
    session = Session()
    configs = session.query(Config).all()
    session.close()
    return configs

def get_config_by_name(name):
    session = Session()
    config = session.query(Config).filter_by(name=name).first()
    session.close()
    return config