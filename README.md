### README: Análise de Marketing Digital

#### Visão Geral

Este projeto envolve a análise de dados de marketing digital coletados de várias plataformas de publicidade online. O objetivo é fornecer insights sobre o custo por lead (CPL), investimentos em campanhas, impressões, sessões, e leads gerados ao longo do tempo. A análise é dividida em várias dimensões, como veículo de marketing, categoria de campanha e períodos de tempo específicos.

#### Estrutura do Dataset

O dataset contém as seguintes colunas:

1. **Veiculo**: Plataforma de publicidade (por exemplo, Google Search, Facebook Ads, Instagram Ads, LinkedIn Ads).
2. **Categoria**: Tipo de campanha (Institucional ou Promocional).
3. **data**: Data específica da entrada.
4. **ano**: Ano da entrada.
5. **mês**: Mês da entrada.
6. **nome do mês**: Nome do mês da entrada.
7. **nome do dia**: Nome do dia da semana da entrada.
8. **Investimento**: Valor investido na campanha (em moeda local).
9. **Leads**: Número de leads gerados.
10. **Sessoes**: Número de sessões geradas.
11. **Impressoes**: Número de impressões geradas.
12. **CPL**: Custo por lead.

#### Descrição dos Gráficos no Painel

1. **Soma de CPL por Ano e Mês**: Este gráfico mostra a soma do custo por lead ao longo dos anos e meses, permitindo identificar tendências e variações sazonais.

2. **Soma de Investimento por Ano e Mês**: Mostra a soma dos investimentos feitos em campanhas de marketing digital ao longo do tempo.

3. **Soma de m�s por Ano e Mês**: Apresenta a soma do mês ao longo dos anos e meses, útil para visualizar a distribuição mensal dos dados.

4. **Soma de CPL por Ano, Mês e Dia**: Este gráfico detalha a soma do custo por lead por ano, mês e dia, fornecendo uma visão granular da variação diária.

5. **Soma de CPL por Veículo**: Mostra a soma do custo por lead para cada plataforma de publicidade, ajudando a identificar quais plataformas são mais eficientes.

6. **Soma de CPL por Categoria**: Compara a soma do custo por lead entre campanhas institucionais e promocionais.

#### Análise Detalhada

1. **Tendências ao Longo do Tempo**:
   - **CPL**: Identificar períodos com aumento ou diminuição do custo por lead pode ajudar a ajustar estratégias de marketing.
   - **Investimento**: Analisar como os investimentos mudaram ao longo do tempo e correlacionar com a eficiência (CPL).

2. **Eficiência por Plataforma**:
   - Comparar o CPL entre diferentes plataformas (Google Search, Facebook Ads, Instagram Ads, LinkedIn Ads) para determinar onde os investimentos são mais eficazes.

3. **Eficiência por Categoria**:
   - Avaliar se campanhas institucionais ou promocionais estão gerando leads a um custo mais baixo.

4. **Análise Granular Diária**:
   - Observar a variação diária do CPL para identificar padrões sazonais ou eventos específicos que impactam a eficiência das campanhas.

#### Conclusão

Este projeto fornece uma visão abrangente dos dados de marketing digital, permitindo uma análise detalhada do desempenho das campanhas em várias dimensões. A análise ajuda a identificar áreas de melhoria e otimizar os investimentos em marketing digital para maximizar a geração de leads a um custo eficiente.

---

### Instruções para Reproduzir a Análise

1. **Carregar os Dados**: Utilize o arquivo CSV fornecido (`marketing_data.csv`) para carregar os dados no ambiente de análise.
2. **Explorar os Dados**: Utilize bibliotecas como pandas para explorar e entender a estrutura dos dados.
3. **Gerar Visualizações**: Utilize ferramentas de visualização de dados como matplotlib, seaborn ou bibliotecas de visualização interativas para criar gráficos similares aos mostrados no painel.
4. **Interpretar os Resultados**: Analise os gráficos e extraia insights relevantes para a tomada de decisões estratégicas em marketing digital.

Seguindo essas etapas, é possível reproduzir e expandir a análise conforme necessário, ajustando as estratégias de marketing com base em dados sólidos e insights detalhados.
