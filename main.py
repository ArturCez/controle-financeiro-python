"""Controle financeiro pessoal simples, executado pelo terminal."""

import json
import math
from pathlib import Path


ARQUIVO_TRANSACOES = Path(__file__).with_name("transacoes.json")


def salvar(transacoes):
    with ARQUIVO_TRANSACOES.open("w", encoding="utf-8") as arquivo:
        json.dump(transacoes, arquivo, indent=4, ensure_ascii=False)


def adicionar_transacao(transacoes, tipo):
    if tipo not in ("receita", "despesa"):
        print("Tipo de transação inválido.")
        return

    descricao = input(f"Descrição da {tipo}: ").strip()
    if not descricao:
        print("Adicione uma descrição.")
        return

    try:
        valor = float(input(f"Valor da {tipo}: ").strip().replace(",", "."))
    except ValueError:
        print("Digite um valor válido.")
        return

    if not math.isfinite(valor) or valor <= 0:
        print("Insira um valor válido.")
        return

    nova_transacao = {
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
    }
    transacoes.append(nova_transacao)
    salvar(transacoes)
    print(f"{tipo.capitalize()} adicionada com sucesso!")


def carregar_transacoes():
    try:
        with ARQUIVO_TRANSACOES.open("r", encoding="utf-8") as arquivo:
            transacoes = json.load(arquivo)
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, UnicodeDecodeError) as erro:
        raise ValueError(
            "O arquivo transacoes.json está inválido. Corrija ou faça uma cópia "
            "antes de executar novamente; nenhum dado foi sobrescrito."
        ) from erro

    if not isinstance(transacoes, list) or any(
        not isinstance(item, dict)
        or item.get("tipo") not in ("receita", "despesa")
        or not isinstance(item.get("descricao"), str)
        or not item["descricao"].strip()
        or type(item.get("valor")) not in (int, float)
        or not math.isfinite(item["valor"])
        or item["valor"] <= 0
        for item in transacoes
    ):
        raise ValueError(
            "O arquivo transacoes.json contém transações inválidas; "
            "nenhum dado foi sobrescrito."
        )
    return transacoes


def listar_transacoes(transacoes):
    if not transacoes:
        print("Nenhuma transação cadastrada.")
        return

    for indice, transacao in enumerate(transacoes, start=1):
        print(
            f"{indice} - {transacao['descricao']} | "
            f"{transacao['tipo']} | R$ {transacao['valor']:.2f}"
        )


def calcular_saldo(transacoes):
    if not transacoes:
        print("Não foi feita nenhuma transação.")
        return

    total_receitas = sum(
        transacao["valor"]
        for transacao in transacoes
        if transacao["tipo"] == "receita"
    )
    total_despesas = sum(
        transacao["valor"]
        for transacao in transacoes
        if transacao["tipo"] == "despesa"
    )
    saldo_total = total_receitas - total_despesas

    print(f"Total de receitas: R$ {total_receitas:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")
    print(f"Saldo disponível: R$ {saldo_total:.2f}")


def menu():
    try:
        transacoes = carregar_transacoes()
    except ValueError as erro:
        print(f"Erro ao carregar transações: {erro}")
        return

    while True:
        print("""
===== CONTROLE FINANCEIRO =====

1 - Adicionar receita
2 - Adicionar despesa
3 - Listar transações
4 - Consultar saldo
5 - Sair

==============================
""")
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                adicionar_transacao(transacoes, "receita")
            case "2":
                adicionar_transacao(transacoes, "despesa")
            case "3":
                listar_transacoes(transacoes)
            case "4":
                calcular_saldo(transacoes)
            case "5":
                print("Encerrando programa...")
                break
            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
