from sqlalchemy import Column, Integer, String

class Restaurants(Base):
    __tablename__ = 'restaurants'
    id = Column(String(8), primary_key=True)
    Lat = Column(Float(40))
    Long = Column(Float(40))

    def __repr__(self)
