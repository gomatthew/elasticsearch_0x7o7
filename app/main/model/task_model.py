from app.main import db


class TaskRecord(db.Model):
    __tablename__ = 'task_record'

    task_id = db.Column(db.Integer, primary_key=True)
    spend_time = db.Column(db.Float)
    start_time = db.Column(db.DateTime)
    finish_time = db.Column(db.DateTime)
    data_rows = db.Column(db.Integer)
    success = db.Column(db.Integer)
    workers = db.Column(db.Integer)
