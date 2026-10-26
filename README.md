# 🔎 Auditoria de Eventos com Python

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte dos meus estudos em Python, com o objetivo de praticar estruturas de dados, estruturas de repetição e manipulação de listas e tuplas por meio de uma simulação de auditoria de logs de acesso.

O programa analisa registros de eventos, identifica inconsistências, filtra dados válidos e destaca ocorrências de erros HTTP 500 e eventos críticos com status 400.

## ⚙️ Funcionalidades

- **Análise de eventos:** contabiliza os registros recebidos.
- **Janela suspeita:** utiliza fatiamento (*slicing*) para selecionar um intervalo específico de eventos.
- **Saneamento de dados:** identifica registros inválidos com base no código de status e na identificação do usuário.
- **Detecção de erros:** conta ocorrências de status HTTP 500 e identifica suas posições na lista.
- **Relatório de eventos críticos:** filtra registros com status 400 e apresenta os resultados em ordem inversa.

## 🛠️ Tecnologias e conceitos utilizados

- Python 3
- Listas e tuplas
- Estruturas condicionais (`if`)
- Laços de repetição (`for`)
- Desempacotamento de tuplas
- `enumerate()`
- Fatiamento de listas (*slicing*)
- `append()` e `len()`

## 🎯 Objetivo de aprendizagem

Consolidar os fundamentos da programação em Python por meio de um exercício prático de análise e organização de dados, desenvolvendo o raciocínio lógico e a capacidade de identificar inconsistências em registros.

## 👩‍💻 Desenvolvido por

Clara Lima — estudante de Análise e Desenvolvimento de Sistemas, em constante aprendizado e evolução na programação.
