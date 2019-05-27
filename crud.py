from basic import db,Puppy

peter=Puppy('tomii',13)

db.session.add_all([peter])

db.session.commit()

print(peter)


#reading from database

print(Puppy.query.all())

# select by id

print(Puppy.query.get(1))


#filter 

puppy_frank=Puppy.query.filter_by(name='frankie')


print(puppy_frank.all())


#####update

pup=Puppy.query.get(1)
pup.age= 10
db.session.add(pup)
db.session.commit()


####delete

pupi=Puppy.query.get(2)
db.session.delete(pupi)
db.session.commit()


print(Puppy.query.all())