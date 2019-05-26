from flask import render_template,request,flash,redirect,url_for,abort
from babacar import app,db
from babacar.models import Student,Classroom
from babacar.forms import SubscribeForm,ClassroomForm
import datetime

def set_student(form,student):
	student.firstname=form.firstname.data
	student.lastname=form.lastname.data
	student.address=form.address.data
	student.birthday=form.birthday.data
	student.number_phone=form.number_phone.data
	student.classroom_id=form.cls.data

@app.route("/")
def home():
	classrooms = Classroom.query.all()
	count_class = classrooms.__len__()
	count_student = Student.query.count()
	return render_template('index.html',classrooms = classrooms,count_class=count_class,count_student=count_student)

@app.route("/<name>/students")
@app.route("/students")
def student_index(name=None):
	if(name):
		classroom = Classroom.query.filter_by(name=name).first()
		if classroom == None:
			abort(404)
		students = Student.query.filter(Student.cls==classroom).all()
	else:
		students = Student.query.all()
	
	classrooms = Classroom.query.all()
	return render_template('/students/index.html',students=students,classrooms=classrooms)

@app.route("/students/new",methods=['GET',"POST"])
def student_new():
	form = SubscribeForm()
	if request.method == "POST":
		if form.validate_on_submit():
			student = Student()
			set_student(form,student)
			db.session.add(student)
			db.session.commit()
			flash("Student has been saved !","success")
			return redirect(url_for('student_index'))

	return render_template('/students/new.html',form=form,legend="Create new Student")

@app.route("/students/<int:id>/edit",methods=['GET',"POST"])
def student_edit(id):
	form = SubscribeForm()
	
	student = Student.query.get_or_404(int(id))
	
	if request.method == "POST":
		if form.validate_on_submit():
			set_student(form,student)
			db.session.commit()
			flash("Student has been midified !","success")
			return redirect(url_for('student_index'))
	form.firstname.data = student.firstname
	form.lastname.data = student.lastname
	form.address.data = student.address
	form.birthday.data = student.birthday
	form.number_phone.data = student.number_phone
	form.cls.data = student.classroom_id
	return render_template('/students/new.html',form=form,student=student,legend=f"Edit Student {student.firstname}  {student.lastname}")

@app.route('/student/<int:id>',methods=['GET',"POST"])
def student_delete(id):
	student = Student.query.get_or_404(id)
	db.session.delete(student)
	db.session.commit()
	flash("student deleted successfuly",'success')
	return redirect(url_for('student_index'))

@app.route('/classroom')
def classroom_index():
	classrooms = Classroom.query.all()
	# for c in classrooms:
	# 	for i in range(1,10):
	# 		s = Student(firstname="name - "+str(i)+c.name,lastname="lastname"+str(i)+c.name,address="address"+str(i)+c.name,classroom_id=c.id,birthday=datetime.date(2000+i,i,i+10))
	# 		db.session.add(s)
	# db.session.commit()
	return render_template('classrooms/index.html',classrooms=classrooms)

@app.route('/classroom/new',methods=['GET','POST'])
def classroom_new():
	form = ClassroomForm()
	if form.validate_on_submit():
		classroom = Classroom(name=form.name.data)
		db.session.add(classroom)
		db.session.commit()
		flash("Classroom Saved successfuly",'success')
		return redirect(url_for('classroom_index'))
	return render_template('classrooms/new.html',form=form,legend="New CLassroom")
@app.route('/classroom/<int:id>/edit',methods=['GET','POST'])
def classroom_edit(id):
	classroom = Classroom.query.get_or_404(id)
	form = ClassroomForm(id)
	if form.validate_on_submit():
		classroom.name = form.name.data
		db.session.commit()
		flash("Classroom modified successfuly",'success')
		return redirect(url_for('classroom_index'))
	form.name.data = classroom.name
	return render_template('classrooms/new.html',form=form,classroom=classroom,legend="Edit CLassroom")
@app.route('/classroom/<int:id>',methods=['GET',"POST"])
def classroom_delete(id):
	classroom = Classroom.query.get_or_404(id)
	db.session.delete(classroom)
	db.session.commit()
	flash("Classroom deleted successfuly",'success')
	return redirect(url_for('classroom_index'))