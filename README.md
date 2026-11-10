# Cálculo de Frete com TDD

Atividade de desenvolvimento de uma função de cálculo de frete em Python utilizando
TDD (Test-Driven Development) com `pytest`.

## Estrutura do projeto

- `frete.py` — implementação da função `calcular_frete`.
- `test_frete.py` — suíte com 12 testes (casos normais, limites e entradas inválidas).
- `README.md` — este documento.

## Regra de negócio

A função recebe o peso em gramas e retorna o valor do frete:

| Faixa de peso                | Valor |
|------------------------------|-------|
| Até 1000 g                   | R$ 10 |
| De 1001 g até 5000 g         | R$ 20 |
| De 5001 g até 10000 g        | R$ 30 |
| Acima de 10000 g             | `ValueError` |

Pesos iguais a zero ou negativos são inválidos e geram `ValueError`.
Pesos acima de 10.000 g também são recusados com `ValueError`
("Produto acima do limite de envio").

## Implementação (`frete.py`)

```python
def calcular_frete(peso_gramas: int) -> int:
    if peso_gramas <= 0:
        raise ValueError("O peso deve ser maior que zero")
    if peso_gramas > 10000:
        raise ValueError("Produto acima do limite de envio")
    if peso_gramas <= 1000:
        return 10
    elif peso_gramas <= 5000:
        return 20
    else:
        return 30
```

## Testes (`test_frete.py`)

Foram escritos 12 testes cobrindo:

- Casos normais: 500 g, 2000 g, 6000 g.
- Limites de faixa: 1 g, 1000 g, 1001 g, 5000 g, 5001 g, 10000 g.
- Entradas inválidas: 0 g, -1 g e 10001 g (esperando `ValueError`).

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
............                                                             [100%]
12 passed
```

## Registro dos ciclos TDD

| Ciclo | Teste                              | Resultado inicial | Depois da implementação |
|-------|------------------------------------|-------------------|--------------------------|
| 1     | Produto de 500 g retorna 10        | Falha             | Passou                   |
| 2     | Produto de 2.000 g retorna 20      | Falha             | Passou                   |
| 3     | Produto de 6.000 g retorna 30      | Falha             | Passou                   |
| 4     | Peso zero gera `ValueError`        | Falha             | Passou                   |
| 5     | Produto de 10.000 g retorna 30     | Passou            | Passou                   |
| 6     | Peso de 10.001 g gera `ValueError` | Falha             | Passou                   |

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
- No desafio adicional, foi incluída a validação de limite máximo: pesos acima de
  10.000 g também geram `ValueError`.
- Os testes foram separados por cenário para facilitar a identificação de erros e
  garantir que os limites das faixas de peso sejam respeitados.

## Desafio adicional (limite de 10.000 g)

A nova regra mantém o cálculo normal até 10.000 g e recusa pesos acima disso.

Ciclo TDD do desafio:

1. 🔴 **Red**: foram adicionados `test_frete_peso_10000g` (deve retornar 30) e
   `test_frete_peso_10001g` (deve lançar `ValueError`). O primeiro já passava com a
   implementação anterior; o segundo falhou com `DID NOT RAISE ValueError`.
2. 🟢 **Green**: foi adicionada a verificação `if peso_gramas > 10000` em `frete.py`,
   lançando `ValueError("Produto acima do limite de envio")`.
3. 🔵 **Refactor**: a estrutura já estava clara e organizada, então nenhuma alteração
   foi necessária apenas por alterar.

Resultado após o desafio: `12 passed`.

## Discussão em sala

1. **Qual teste você escreveu primeiro? Por quê?**
   Primeiro escrevi o teste de 500 g, porque era o primeiro caso apresentado na
   atividade e permitia implementar a funcionalidade mais simples.

2. **Quando o código passou, mas ainda faltavam regras?**
   Quando o teste inicial de 500 g passou, mas ainda não tínhamos testado as outras
   faixas de peso nem os pesos inválidos.

3. **Qual caso de fronteira revelou um erro?**
   O teste de 10.001 g revelou que o sistema ainda aceitava produtos acima do limite
   permitido de envio.

4. **Qual mudança foi refatoração e qual alterou a regra?**
   A refatoração seria melhorar a organização do código sem mudar seu comportamento.
   Já adicionar a validação de peso acima de 10.000 g alterou a regra de negócio.

## Ciclo Red → Green → Refactor

1. 🔴 **Red**: escrever o teste e observar sua falha.
2. 🟢 **Green**: implementar o mínimo necessário para passar.
3. 🔵 **Refactor**: melhorar o código sem alterar o comportamento.

Essa sequência foi repetida para cada novo cenário da atividade.
