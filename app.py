import streamlit as st

st.title("Calculadora de Custo Fabric/Power BI")


dash_name = st.text_input("Nome do Dashboard", "")


plano = st.segmented_control("Plano de Referência", ["F4", "F8"], default="F4")

st.markdown("### Critérios Técnicos")
st.caption("Selecione o nível de 1 a 5 para cada item abaixo:")


v_dados = st.segmented_control("Volume de Dados (1: Poucas linhas | 5: Milhões de linhas)", [1, 2, 3, 4, 5], default=1)
c_transf = st.segmented_control("Complexidade de Transformação (1: Carga simples | 5: Muitas regras/merges)", [1, 2, 3, 4, 5], default=1)
f_atualiz = st.segmented_control("Frequência de Atualização (1: Semanal/mensal | 5: Diária ou mais)", [1, 2, 3, 4, 5], default=1)
c_dax = st.segmented_control("Complexidade DAX/Modelagem (1: Medidas simples | 5: Cálculos pesados)", [1, 2, 3, 4, 5], default=1)
audiencia = st.segmented_control("Audiência Esperada (1: 1 a 3 usuários | 5: Muitos usuários/externo)", [1, 2, 3, 4, 5], default=1)
rls = st.segmented_control("RLS/Segurança (1: Sem RLS | 5: RLS por filial/contrato)", [1, 2, 3, 4, 5], default=1)
criticidade = st.segmented_control("Criticidade Operacional (1: Consulta eventual | 5: Operação crítica/diretoria)", [1, 2, 3, 4, 5], default=1)


score = (v_dados * 0.20) + (c_transf * 0.20) + (f_atualiz * 0.15) + (c_dax * 0.15) + (audiencia * 0.10) + (rls * 0.10) + (criticidade * 0.10)

if score < 2.0:
    porte = "Muito pequeno"
    custo = "R\$ 35 a R\$ 105" if plano == "F4" else "R\$ 67 a R\$ 201"
elif score < 3.0:
    porte = "Pequeno"
    custo = "R\$ 105 a R\$ 175" if plano == "F4" else "R\$ 201 a R\$ 335"
elif score < 3.8:
    porte = "Médio"
    custo = "R\$ 210 a R\$ 350" if plano == "F4" else "R\$ 402 a R\$ 670"
elif score < 4.5:
    porte = "Grande"
    custo = "R\$ 385 a R\$ 700" if plano == "F4" else "R\$ 737 a R\$ 1.340"
else:
    porte = "Crítico/Pesado"
    custo = "R\$ 735 a R\$ 1.225+" if plano == "F4" else "R\$ 1.407 a R\$ 2.345+"

st.divider()
st.subheader("Resultado da Estimativa")


st.info(f"**Porte Estimado:** {porte} | **Custo Estimado ({plano}):** {custo}")