# Calculadora de Custo Fabric e Power BI

## Propósito Geral
Esta ferramenta foi desenvolvida para estimar o custo técnico mensal de novos projetos em Power BI antes do início do desenvolvimento. O objetivo é servir como uma régua prática de governança para apoiar a tomada de decisão, priorização e direcionamento de demandas na ocupação da capacidade Fabric (cenários F4 e F8).

## Link de Acesso
[Acesse por aqui](https://calculadora-fabric.streamlit.app/)

## Metodologia de Cálculo

O sistema calcula um Score Técnico Ponderado com base em 7 critérios preenchidos pelo usuário (com notas de 1 a 5):

* **Volume de dados** (Peso: 20%)
* **Complexidade de transformação** (Peso: 20%)
* **Frequência de atualização** (Peso: 15%)
* **Complexidade DAX/modelagem** (Peso: 15%)
* **Audiência esperada** (Peso: 10%)
* **RLS/segurança** (Peso: 10%)
* **Criticidade operacional** (Peso: 10%)

### Fórmula do Score Final

Score Final = (Volume * 0.20) + (Transformação * 0.20) + (Frequência * 0.15) + (DAX * 0.15) + (Audiência * 0.10) + (RLS * 0.10) + (Criticidade * 0.10)