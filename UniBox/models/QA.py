from sqlalchemy import Column, String, Integer


from .meta import Base


class QA(Base):
    __tablename__ = 'q&a'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

def __repr__(self):
    return '<QA(question = "{}", answer = "{}">', format(self.question, self.answer)
