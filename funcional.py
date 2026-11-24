
"""
Semana 3 — Reescrevendo com programação funcional

Conceitos: funções puras, imutabilidade, map, filter, sorted e lambda.
"""

from collections import namedtuple

# Constantes
ALIQUOTA_PADRAO = 0.25

ALIQUOTAS = {
    "cesta_basica": 0.0,
    "reduzido": 0.10,
    "padrao": 0.25
}

# Estrutura dos itens
Item = namedtuple(
    "Item",
    ["nome", "preco", "categoria", "quantidade"],
    defaults=[1]
)


def aliquota(categoria):
    """Retorna a alíquota correspondente à categoria."""
    if categoria not in ALIQUOTAS:
        raise ValueError("Categoria inválida.")

    return ALIQUOTAS[categoria]


def imposto_item(item):
    """Calcula o imposto de acordo com a categoria e quantidade."""
    return round(
        round(item.preco * aliquota(item.categoria), 2)
        * item.quantidade,
        2
    )


def total_impostos(itens):
    """Calcula a soma dos impostos de todos os itens usando map."""
    return round(sum(map(imposto_item, itens)), 2)


def total_compra(itens):
    """Calcula o valor total da compra com impostos."""
    subtotal = sum(
        map(lambda item: item.preco * item.quantidade, itens)
    )

    return round(subtotal + total_impostos(itens), 2)


def filtrar_por_categoria(itens, categoria):
    """Retorna uma lista com os itens da categoria escolhida."""
    return list(
        filter(lambda item: item.categoria == categoria, itens)
    )


def ordenar_por_preco(itens, decrescente=False):
    """Ordena os itens pelo preço unitário."""
    return sorted(
        itens,
        key=lambda item: item.preco,
        reverse=decrescente
    )


def economia_total(itens):
    """Calcula quanto o consumidor economizou com a redução dos impostos."""
    imposto_padrao = sum(
        map(
            lambda item: round(
                item.preco * ALIQUOTA_PADRAO, 2
            ) * item.quantidade,
            itens
        )
    )

    return round(imposto_padrao - total_impostos(itens), 2)


if __name__ == "__main__":
    itens = [
        Item("Arroz 5kg", 25.90, "cesta_basica", 1),
        Item("Chocolate", 10.00, "padrao", 2),
        Item("Biscoito", 5.00, "reduzido", 3)
    ]

    print("Impostos:", total_impostos(itens))
    print("Total da compra:", total_compra(itens))
    print("Economia:", economia_total(itens))

    print("\nItens da cesta básica:")
    print(filtrar_por_categoria(itens, "cesta_basica"))

    print("\nItens ordenados por preço:")
    print(ordenar_por_preco(itens))
