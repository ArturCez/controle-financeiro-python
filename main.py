import json


def salvar(transacoes):
    with open("transacoes.json", "w", encoding="utf-8") as arquivo:
        json.dump(transacoes, arquivo, indent=4, ensure_ascii=False)

def adicionar_transacao(transacoes, tipo):
    if tipo not in ("receita", "despesa"):
        print("Tipo de transação inválido.")
        return
    descricao = input(f"Descrição da {tipo}: ").strip()
    if not descricao:
        print("Adicione uma descrição. ")
        return
    try:
        valor = float(input(f"Valor da {tipo}: ").replace(",", "."))
        if valor <= 0:
            print("Insira um valor válido.")
            return
    except ValueError:
        print("Digite um valor válido. ")
        return
    nova_transacao = {
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo
    }
    transacoes.append(nova_transacao)
    salvar(transacoes)
    print(f"{tipo.capitalize()} adicionada com sucesso!")

def carregar_transacoes():
    try:
        with open("transacoes.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]

def listar_transacoes(transacoes):
    if not transacoes:
        print("Nenhuma transação cadastrada. ")
        return

    for i, transacao in enumerate(transacoes, start = 1):
        print(f"{i} - {transacao['descricao']} | {transacao['tipo']} | R$ {transacao['valor']:.2f}")

def calcular_saldo(transacoes):

    if not transacoes:
        print("Não foi feita nenhuma transação")
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
    transacoes = carregar_transacoes()
    while True:

        print("""
    ===== CONTROLE FINANCEIRO =====

    1 - Adicionar receita
    2 - Adicionar despesa
    3 - listar transações 
    4 - Consultar saldo
    5 - sair

    ===============================
        """)

        opcao = (input("Escolha uma opção: ")).strip()

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
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

    
