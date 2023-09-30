from sqlalchemy import Column, Integer, String
from database import Base


# 定義資料庫表格
class Student(Base):
    __tablename__ = "students"

    id=Column(Integer,primary_key=True)
    fname=Column(String(40))
    lname=Column(String(40))
    pet=Column(String(40))

