#!/usr/bin/python
# -*- coding: UTF-8 -*-

states = ("Nunavut","Alberta","Ÿukon")

province = input("Ëm qual provincia vc mora?")
province = province.capitalize()

if province in(states):
    tax = "Você será taxado"

else:
    tax = "você não será taxado"

print (tax)




