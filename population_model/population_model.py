#!/bin/python

import random

class person:
  'a single person'
  person_count=0
  
  def __init__(self, name,age,sex,number_of_children):
    self.name=name
    self.age=age
    self.sex=sex
    self.number_of_children=number_of_children
    person.person_count += 1
    
  def displayCount(self):
    print("population=%d" % person.person_count)
    
  def displayPerson(self):
    print "Name=",self.name,", age in days=",self.age,", sex=",self.sex,", kid count=",self.number_of_children

initial_number_of_people=100
birth_rate=0.0001
death_rate=0.0001

# create an initial population with distribution of ages

population=[]
for indx in range(initial_number_of_people):
  this_person=person("Ben",random.randint(1,36500),"male",random.randint(0,4))
  population.append(this_person)

population[0].displayPerson()
population[0].displayCount()
print len(population)
print "my age=",population[0].age

for day in range(3650):
  if ((day % 365)==0):
    print("year="+str(day/365))
    print("population="+str(len(population)))	
  remove_this_person=[]
  add_this_person=[]
  for this_person_indx in range(len(population)): # increment each person's age
    population[this_person_indx].age = population[this_person_indx].age+1

    this_person_has_baby=False
    birth_coin=random.random() # coin flip for having a kid
    # re-shape this distribution such that you are most likely to have a kid between 15, 35
    if (birth_coin < birth_rate):
      this_person_has_baby=True
    if (this_person_has_baby): 
      population[this_person_indx].number_of_children += 1
      add_this_person.append(1)

    this_person_dies=False
    death_coin=random.random()# coin flip for death
    # re-shape this distribution such that you are more likely to die as you age
    if (death_coin < death_rate): 
      this_person_dies=True
    if (this_person_dies):
      remove_this_person.append(this_person_indx)
      #print("person survived today")
  for indx in range(len(remove_this_person)):
    print("     remove person "+str(remove_this_person[indx]))
    population.pop(remove_this_person[indx])
  for indx in range(len(add_this_person)):
    print("     add person ")
    new_kid_age=0 
    new_kid_number_of_kids=0
    new_person=person("Ben",new_kid_age,"male",new_kid_number_of_kids)
    population.append(this_person)    
  
population[0].displayPerson()
print population[0].age
