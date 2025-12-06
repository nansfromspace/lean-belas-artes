# Jogo de bingo

## Descrição

Este é um simulador de jogo de bingo desenvolvido como projeto para aplicação de conceitos de Lean e melhoria contínua no desenvolvimento de software.

---

## Funcionalidades
**Sorteio de bolas**
- Sistema que sorteia números de 1 a 75
- Cada número só pode ser sorteado uma vez
- Exibição clara do número sorteado com letra correspondente (B-I-N-G-O)

**Geração de cartela**
- Cartela com 24 números + 1 espaço livre (formato 5x5)
- Respeita as regras das colunas:
  - B: números 1-15
  - I: números 16-30
  - N: números 31-45
  - G: números 46-60
  - O: números 61-75

**Simulação de jogada**
- Marcação automática dos números sorteados
- Verificação de vitória
- Exibição visual da cartela
- Estatísticas da partida
- Histórico de números sorteados

---

## Como usar

### Pré-requisitos
- Python 3.7 ou superior

### Executando o Jogo

```bash
python bingo.py
```

O jogo irá:
1. Mostrar sua cartela inicial
2. Aguardar você pressionar ENTER para começar
3. Sortear números um por um
4. Marcar automaticamente se o número está na sua cartela
5. Continuar até você ganhar (completar todos os 24 números)
6. Mostrar estatísticas finais da partida

---

## Conceitos aplicados

### Programação orientada a objetos
- **SorteadorBingo**: Gerencia o sorteio dos números
- **CartelaBingo**: Gerencia a cartela e marcações
- **JogoBingo**: Orquestra o jogo completo

### Estruturas de dados
- Listas para armazenar números
- Sets para números marcados (evita duplicatas)
- Type hints para clareza do código

### Lean e Melhoria contínua
- Código simples e direto (eliminar desperdícios)
- Qualidade desde o início (validações)
- Entregas incrementais (MVP funcional)
- Decisões flexíveis (parâmetros configuráveis)
- Respeito às pessoas (código legível)

---

## Sobre o desenvolvimento

Este projeto foi desenvolvido seguindo princípios Lean:

1. **MVP primeiro**: Versão funcional básica
2. **Código limpo**: Legível e bem estruturado
3. **Sem over-engineering**: Só o necessário
4. **Validações adequadas**: Qualidade desde o início
5. **Documentação útil**: Clara e objetiva

---

## Observações


Este código foi desenvolvido apenas para:
- Fins educacionais
- Demonstração de conceitos de programação
- Aplicação prática de metodologias Lean
- Estudo de estruturas de dados e algoritmos

---

**Desenvolvido como projeto acadêmico - Faculdade Belas Artes - 2025**
