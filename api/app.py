from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import SessionLocal, engine
from models import Base
import os
from datetime import time
from flask_migrate import Migrate
import psycopg2


Base.metadata.create_all(bind=engine)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')

db=SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
  __tablename__='students'
  id=db.Column(db.Integer,primary_key=True)
  fname=db.Column(db.String(40))
  lname=db.Column(db.String(40))
  pet=db.Column(db.String(40))
  personals = db.relationship("Personal", backref="personal")

  def __init__(self,fname,lname,pet):
    self.fname=fname
    self.lname=lname
    self.pet=pet

class Personal(db.Model):
    __tablename__ = 'personal'
    id = db.Column(db.Integer, primary_key=True)   
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.route('/studentForm')
def index():
  return render_template('index.html')

@app.route('/getStudent/<id>')
def getStudent(id):
  assert id == request.view_args['id']
  studentResult=db.session.query(Student).filter(Student.id==id)
  data = {}
  for result in studentResult:
    data = {
       "id":result.id,
       "fname": result.fname,
       "lname":result.lname,
       "pet":result.pet
    }

  print(data)

  return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit():
  fname= request.form['fname']
  lname=request.form['lname']
  pet=request.form['pets']

  student=Student(fname,lname,pet)
  db.session.add(student)
  db.session.commit()

  #fetch a certain student2
  studentResult=db.session.query(Student).filter(Student.id==1)
  for result in studentResult:
    print(result.fname)

  return render_template('success.html', data=fname)


# ================= Not ORM =================
keys = ['CampaignId', 'Title', 'Content', 'maxMembers', 'minMembers', 'Owner', 'CreateAt', 'StartAt', 'EndAt', 'Available', 'status']

def preprocess_data(data_tuple):
    processed_data = []
    for item in data_tuple:
        if isinstance(item, time):
            processed_data.append(item.strftime('%H:%M:%S'))
        else:
            processed_data.append(item)
    return tuple(processed_data)


def get_db_connection():
    conn = psycopg2.connect(host=os.getenv('POSTGRES_HOST'),
                            port=os.getenv('DB_PORT'),
                            database=os.getenv('POSTGRES_DATABASE'),
                            user=os.getenv('POSTGRES_USER'),
                            password=os.getenv('POSTGRES_PASSWORD')
    )
    return conn

@app.route("/")
def hello_world():
    return "<p>Welcome To The Fionn Page</p>"


@app.route('/campaign')
def test():
    conn = get_db_connection()

    cur = conn.cursor()

    cur.execute('SELECT * FROM campaign')
    
    data = cur.fetchall()
    
    cur.close()
    conn.close()
    print(data[0])
    processed_data = preprocess_data(data[0])
    data_dict = dict(zip(keys, processed_data))
    
    return jsonify(data_dict)
# ================= Not ORM =================


if __name__ == '__main__': 
 
  app.run(debug=True)
