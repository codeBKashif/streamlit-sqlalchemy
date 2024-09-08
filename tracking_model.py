from sqlalchemy import Column, Integer, String, Enum
from db_connection import Base
from constants import Gender


# Define a mapping between the table columns and the data editor columns
user_editor_mapping = {
    "Name": "name",
    "Age": "age",
    "Gender": "gender"
}

# Define a sample table model using SQLAlchemy ORM
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(Enum(Gender))

    def to_dict(self):
        return {"id": self.id, "Name": self.name, "Age": self.age, "Gender": self.gender.value if self.gender else None}
    
    def from_dict(self, data):
        for key, value in data.items():
            setattr(self, user_editor_mapping[key], value)
    


def add_user(data):
    user = User()
    user.from_dict(data)
    return user