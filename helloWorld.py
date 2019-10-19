from datetime import datetime, timedelta

print()
print()

aniversario = input("Qual o dia do seu aniversário (dd/mm/aa)?")
msg = "O ano do seu nascimento é: "

try:
    aniversario_date = datetime.strptime(aniversario,"%d/%m/%Y")
except ValueError as e:
    print("A data foi digitada errada")
    print(aniversario)
    msg = "Vê se digita essa merda certo dessa vez..."
finally:
    print(msg)
    


try:
    print(aniversario_date.year)
except NameError as e:
    pass
else:
    pass
finally:
    pass 


print()
print()









