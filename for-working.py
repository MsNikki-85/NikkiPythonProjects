#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals:
    if pet == 'dog': continue #can add hashtag in front will change tyrp of loop
    if pet == 'velociraptor': break #can add hashtag in front will change tyrp of loop
    print(pet)
else:
    print('that is all of the animals')
