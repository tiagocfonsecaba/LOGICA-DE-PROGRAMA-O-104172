import os
os.system ("cls")

kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (em Kg): "))


if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20


if kg_maca <= 5:
      preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50


total_kg = kg_morango + kg_maca
total_pago = preco_morango + preco_maca


if total_kg >= 10 or total_pago > 15.00:
    total_pago = total_pago * 0.90


print(f"Valor total a ser pago: R$ {total_pago:.2f}")