from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from database import Base
from sqlalchemy.dialects.postgresql import UUID,JSONB
from sqlalchemy.types import SmallInteger,Text



# 定義資料庫表格
class Student(Base):
    __tablename__ = "students"

    id=Column(Integer,primary_key=True)
    fname=Column(String(40))
    lname=Column(String(40))
    pet=Column(String(40))

class Personal(Base):
    __tablename__ = 'personal'
    id = Column(Integer, primary_key=True)   
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)


class Campaign(Base):
    __tablename__ = "campaign"

    Available=Column(Boolean)
    Content=Column(JSONB)
    CreateAt=Column(DateTime(timezone=True))
    EndAt=Column(DateTime(timezone=True))
    CampaignId=Column(UUID(as_uuid=True), primary_key=True)
    Owner=Column(UUID(as_uuid=True))
    StartAt=Column(DateTime(timezone=True))
    Title=Column(Text)
    maxMembers=Column(SmallInteger)
    minMembers=Column(SmallInteger)
    status=Column(Text)


# uuid jsonb smallint smallint uuid time with time zone, time with time zone,  time with time zone, bool, text