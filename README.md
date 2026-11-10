# Cálculo de Frete com TDD

Atividade de desenvolvimento de uma função de cálculo de frete em Python utilizando
TDD (Test-Driven Development) com `pytest`.

## Estrutura do projeto

- `frete.py` — implementação da função `calcular_frete`.
- `test_frete.py` — suíte com 10 testes (casos normais, limites e entradas inválidas).
- `README.md` — este documento.

## Regra de negócio

A função recebe o peso em gramas e retorna o valor do frete:

| Faixa de peso            | Valor |
|--------------------------|-------|
| Até 1000 g               | R$ 10 |
| De 1001 g até 5000 g     | R$ 20 |
| Acima de 5000 g          | R$ 30 |

Pesos iguais a zero ou negativos são inválidos e geram `ValueError`.

## Implementação (`frete.py`)

```python
def calcular_frete(peso_gramas: int) -> int:
    if peso_gramas <= 0:
        raise ValueError("O peso deve ser maior que zero")
    if peso_gramas <= 1000:
        return 10
    elif peso_gramas <= 5000:
        return 20
    else:
        return 30
```

## Testes (`test_frete.py`)

Foram escritos 10 testes cobrindo:

- Casos normais: 500 g, 2000 g, 6000 g.
- Limites de faixa: 1 g, 1000 g, 1001 g, 5000 g, 5001 g.
- Entradas inválidas: 0 g e -1 g (esperando `ValueError`).

## Como executar

### 1. Criar o ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
```

Windows:

```bat
python -m venv .venv
```

### 2. Ativar o ambiente virtual

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows (Prompt de Comando):

```bat
.venv\Scripts\activate.bat
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

> Se o PowerShell bloquear o script, rode uma vez:
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

Após ativar, o terminal exibe `(.venv)` no início da linha.

### 3. Instalar o pytest e rodar os testes

```bash
pip install pytest
python -m pytest -q
```

### 4. Sair do ambiente virtual

```bash
deactivate
```

Resultado esperado:

```text
..........                                                               [100%]
10 passed
```

## Registro dos ciclos TDD

| Ciclo | Teste                              | Resultado inicial | Depois da implementação |
|-------|------------------------------------|-------------------|--------------------------|
| 1     | Produto de 500 g retorna 10        | Falha             | Passou                   |
| 2     | Produto de 2.000 g retorna 20      | Falha             | Passou                   |
| 3     | Produto de 6.000 g retorna 30      | Falha             | Passou                   |
| 4     | Peso zero gera `ValueError`        | Falha             | Passou                   |

### Explicação da falha inicial

No início, a função ainda não estava implementada (ou lançava `NotImplementedError`),
então cada novo teste falhava antes da lógica correspondente existir.

### Explicação do sucesso

Após implementar a lógica mínima necessária para cada regra de frete, o teste passou.
O ciclo foi repetido para cada novo cenário até cobrir todas as faixas e validações.

## Decisão de implementação/refatoração

- A implementação foi organizada com estruturas condicionais (`if`, `elif` e `else`)
  para separar as três faixas de peso de forma clara.
- Foi adicionada uma validação para impedir pesos iguais a zero ou negativos,
  lançando `ValueError`.
- Os testes foram separados por cenário para facilitar a identificação de erros e
  garantir que os limites das faixas de peso sejam respeitados.

## Ciclo Red → Green → Refactor

1. 🔴 **Red**: escrever o teste e observar sua falha.
2. 🟢 **Green**: implementar o mínimo necessário para passar.
3. 🔵 **Refactor**: melhorar o código sem alterar o comportamento.

Essa sequência foi repetida para cada novo cenário da atividade.
