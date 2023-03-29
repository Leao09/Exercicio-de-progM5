from models.base import Base
from sqlalchemy import Column, Float, Integer


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    rot = Column(Float)

    def __init__(self, x, y, z, rotation):
        self.x = x
        self.y = y
        self.z = z
        self.rot = rotation

    def as_json(self):
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "rot": self.rot
        }

    def __repr__(self) -> str:
        return f"passo = {self.id}, x = {self.x}, y = {self.y}, z = {self.z}, rotation = {self.rot}"
