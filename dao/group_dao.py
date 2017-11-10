from sqlalchemy import *
from sqlalchemy.sql import select

DATABASEURI = "postgresql://ky2371:naruhodo@35.196.90.148/proj1part2"
db = create_engine(DATABASEURI)
db.echo = False  #No logging
metadata = MetaData(db)

#Print result
def run(stmt):
	rs = stmt.execute()
	for row in rs:
		print(row)

membership = Table('membership', metadata, autoload = True)
f_user = select([membership.c.member_id,membership.c.since], membership.c.circle_id == 1).alias("f_user")
student = Table('student', metadata, autoload = True)
school = Table('school', metadata, autoload=True)
s = select([student.c.user_id,student.c.nick_name,student.c.avatar,school.c.school_id,school.c.school_name,],and_(student.c.user_id==f_user.c.member_id, \
	student.c.school_id==school.c.school_id)).order_by(f_user.c.since).limit(2)
run(s)
