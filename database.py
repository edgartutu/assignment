from basic import db,Puppy


#creat all tables

db.create_all()

sam=Puppy('SAMMY',3)

frank=Puppy('frankie',4)



db.session.add_all([sam,frank])
db.session.commit()

print(sam.id)

print(frank.id)