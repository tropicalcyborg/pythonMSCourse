from datetime import datetime, timedelta

print()
print()

aniversario = input("Qual o dia do seu aniversário (dd/mm/aa)?")
aniversario_date = datetime.strptime(aniversario,"%d/%m/%Y")
#print(str(aniversario_date))

trintaDiasAMais = timedelta(days=30)
try:
    print(trintaDiasAMais)
except "time data '\x1b[A' does not match format '%d/%m/%Y'" as e:
    print("Você digitou a data em formato errrado")
finally:
    print("Tente novamente")

desaniversario = aniversario_date + trintaDiasAMais
print(str(desaniversario.date()))

print()
print()









