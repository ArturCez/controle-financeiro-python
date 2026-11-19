# Controle Financeiro Pessoal em Python

Aplicação de linha de comando para registrar receitas e despesas, consultar movimentações e acompanhar o saldo disponível. Os dados ficam salvos localmente em um arquivo JSON, permanecendo disponíveis entre execuções.

Projeto desenvolvido para praticar os fundamentos de Python e evoluir gradualmente para funcionalidades mais completas.

## Funcionalidades

- Adicionar receitas e despesas com descrição e valor.
- Validar descrições vazias, valores não numéricos, zero e negativos.
- Aceitar valores digitados com ponto ou vírgula decimal (`25.50` ou `25,50`).
- Listar transações numeradas.
- Calcular o total de receitas, despesas e o saldo.
- Salvar e carregar transações em `transacoes.json`.

## Tecnologias

- Python **3.10 ou superior** (por utilizar `match/case`).
- Biblioteca padrão do Python: `json`.
- Sem dependências externas.

## Como executar

1. Instale [Python](https://www.python.org/downloads/) 3.10 ou superior.
2. Baixe ou clone o repositório e abra um terminal na pasta do projeto.
3. Execute:

   ```bash
   python main.py
   ```

   Em alguns sistemas, o comando pode ser `python3 main.py`.

## Exemplo de uso

```text
===== CONTROLE FINANCEIRO =====

1 - Adicionar receita
2 - Adicionar despesa
3 - Listar transações
4 - Consultar saldo
5 - Sair

Escolha uma opção: 1
Descrição da receita: Salário
Valor da receita: 2500,00
Receita adicionada com sucesso!

Escolha uma opção: 2
Descrição da despesa: Mercado
Valor da despesa: 350,50
Despesa adicionada com sucesso!

Escolha uma opção: 4
Total de receitas: R$ 2500.00
Total de despesas: R$ 350.50
Saldo disponível: R$ 2149.50
```

*Exemplo ilustrativo com uma lista inicialmente vazia. A aplicação exibe valores com ponto decimal e duas casas.*

## Estrutura do projeto

```text
controle-financeiro/
├── main.py
├── README.md
└── .gitignore
```

O arquivo `transacoes.json` é criado automaticamente ao registrar a primeira transação. Ele não é incluído no repositório para evitar a publicação de dados financeiros pessoais.

## Como os dados são armazenados

Cada transação é representada por um dicionário dentro de uma lista JSON:

```json
[
    {
        "descricao": "Salário",
        "valor": 2500.0,
        "tipo": "receita"
    },
    {
        "descricao": "Mercado",
        "valor": 350.5,
        "tipo": "despesa"
    }
]
```

Se o arquivo não existir, o programa começa com uma lista vazia. O tratamento de arquivos JSON inválidos ou corrompidos ainda não foi implementado.

## Limitações conhecidas e próximos passos

Esta é uma aplicação educacional. A versão atual ainda não permite editar, excluir, categorizar nem filtrar transações. Como os valores utilizam `float`, não é indicada para cálculos financeiros que exijam precisão contábil; uma evolução futura pode utilizar `decimal.Decimal`.

Melhorias planejadas:

- [ ] Remover e editar transações.
- [ ] Registrar datas e categorias.
- [ ] Filtrar por período e gerar relatórios.
- [ ] Adicionar testes automatizados.
- [ ] Melhorar a validação de dados e o tratamento de erros.
- [ ] Utilizar `Decimal` para valores monetários.
- [ ] Avaliar migração do JSON para SQLite.

## Autor

Projeto de estudo desenvolvido por **Artur Cezar**.
