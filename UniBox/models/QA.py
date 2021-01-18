from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///bot.db")


base = declarative_base()


class QA(base):
    __tablename__ = 'q&a'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

def __repr__(self):
    return '<QA(question = "{}", answer = "{}">', format(self.question, self.answer)
