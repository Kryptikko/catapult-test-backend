# -*- coding: utf-8 -*-
from sqlalchemy import Integer, Column, create_engine, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

DB_CONFIG = {
    "host":"sqlite:////tmp/test.db",
    "user":"root",
    "passwd":"password",
    "db":"catapult"
}


Base = declarative_base()
engine = create_engine(DB_CONFIG["host"], echo=True)
sess = Session(engine)
