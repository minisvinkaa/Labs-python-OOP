# A software academy teaches two types of courses:
# local courses that are held in some of the academy’s local labs
# and offsite courses held in some other town outside of the academy’s headquarters.
# Each course has a name, a teacher assigned to teach it and a course program (sequence of topics).
# Each teacher has a name and knows the courses he or she teaches.
# Both courses and teachers could be printed in human-readable text form.
# All your courses should implement ICourse. Teachers should implement ITeacher.
# Local and offsite courses should implement ILocalCourse and IOffsiteCourse respectively.
# Courses and teachers should be created only through
# the ICourseFactory interface implemented by a class named CourseFactory.
# Write a program that will form courses of software academy.


from lab4.task3.classes.CourseFactory import CourseFactory


if __name__ == "__main__":

    factory = CourseFactory()
    factory.form_course('OOP', 'Lilia Marsovna', ['Classes', 'Decorators', 'Iterators'], 'local')
    factory.form_course('Java', 'Lilia Marsovna', ['Arrays', 'Methods'], 'local')
    factory.form_course('Databases', 'Lolik Fimovich', ['Tables', 'Commands'], 'offsite')

    for course in factory:
        print(course)



