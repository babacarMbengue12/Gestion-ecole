from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError,Required
from babacar.models import Classroom

def getChoices():

	classes = Classroom.query.all()
	c = []
	for cl in classes:
		c.append((cl.id,cl.name))
	return c

class SubscribeForm(FlaskForm):

	firstname = StringField('Firstname',validators=[DataRequired(),Length(min=2,max=60)])
	lastname = StringField("Lastname",validators=[DataRequired(),Length(min=2,max=60)])
	address = StringField('Address (optional)')
	number_phone = StringField('Number phone (optional)')
	cls = SelectField("Classroom",coerce=int,choices=getChoices())
	birthday = DateField('Date',format='%Y-%m-%d',validators=[DataRequired()])
	btn = SubmitField("Enregistrer")

	def validate_cls(self,cl):
		if not cl.data:
			raise ValidationError("Please choise A valid Classroom")
	

class ClassroomForm(FlaskForm):
	name = StringField('Name',validators=[DataRequired(),Length(min=2,max=60)])
	btn = SubmitField("Enregistrer")
	def __init__(self,id = None):
		self.id = id
		super(ClassroomForm,self).__init__()
	def validate_name(self,name):
		if self.id:
			classroom = Classroom.query.filter(Classroom.name==name.data,Classroom.id != self.id).first()
		else:
			classroom = Classroom.query.filter(Classroom.name==name.data).first()
		if classroom != None:
			raise ValidationError('this name is already exist in database')