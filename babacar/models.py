from babacar import db

class Classroom(db.Model):

	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(60), nullable=False)

	students = db.relationship('Student',backref='cls',lazy=True)

	def __repr__(self):
		return f"Classroom('{self.name}','{self.students}')"

class Student(db.Model):

	id = db.Column(db.Integer, primary_key=True)

	firstname = db.Column(db.String(60), nullable=False)
	lastname = db.Column(db.String(60), nullable=False)
	birthday = db.Column(db.Date(), nullable=False)
	address = db.Column(db.String(60), nullable=True)
	number_phone = db.Column(db.String(60), nullable=True)
	classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'), nullable=False)

	def __repr__(self):
		return f"Student('{self.firstname}','{self.lastname}','{self.birthday}','{self.address}','{self.number_phone}','{self.classroom_id}')"
