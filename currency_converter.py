pesos = float(input('How many Pesos left over? '))
soles = float(input('How many Soles left over? '))
reais= float(input('How many Reais left over? '))

pesos_exch = pesos/4157
soles_exch = soles/3.75
reais_exch = reais/5.45

total_usd = pesos_exch + soles_exch + reais_exch

print(f'Remaining balance from Pesos: $ {pesos_exch:.2f}')
print(f'Remaining balance from Soles: $ {soles_exch:.2f}')
print(f'Remaining balance from Reais: $ {reais_exch:.2f}')


print(f'Total in USD: $ {total_usd:.2f}')
