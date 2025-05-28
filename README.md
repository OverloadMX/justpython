# Sistema Bancário 🏦

Bem-vindo ao **Sistema Bancário**, uma aplicação simples desenvolvida em Python para simular operações financeiras básicas. Este projeto foi criado como parte de uma prova de conceito (POC) e oferece funcionalidades essenciais para gerenciar uma conta bancária.

---

## 🌟 Funcionalidades

O sistema bancário permite que você realize as seguintes operações:

1. **💸 Sacar Dinheiro**:
   - Retire valores do saldo disponível.
   - Respeite o limite diário de saques e o valor máximo permitido por saque.
   - Atualize o saldo e registre o saque no extrato.

2. **💰 Depositar Dinheiro**:
   - Adicione valores à sua conta.
   - Atualize o saldo e registre o depósito no extrato.

3. **📜 Consultar Saldo e Extrato**:
   - Visualize o saldo atual da sua conta.
   - Confira o histórico de transações realizadas (saques e depósitos).

4. **🚪 Encerrar o Sistema**:
   - Saia do sistema bancário com segurança.

---

## 📋 Regras do Sistema

- **Limite de Saques**:
  - O número de saques diários é limitado.
  - O valor máximo permitido por saque é definido pela constante `LIMITE_SAQUE`.

- **Validação de Valores**:
  - O sistema valida os valores inseridos pelo usuário, garantindo que sejam numéricos e estejam dentro dos limites permitidos.

- **Saldo Insuficiente**:
  - O sistema impede saques que excedam o saldo disponível.

---

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou copie o arquivo `sistemabancario.py` para o seu ambiente local.
3. Execute o arquivo no terminal:
   ```bash
   python sistemabancario.py
