# imoveisml

Algoritmos lineares e não lineares de aprendizagem de máquina para estimar valores de imóveis de maneira interpretável.

As bases de dados utilizadas para treinamento e teste dos algoritmos são híbridas e contêm atributos de imóveis da União avaliados e homologados pelo Exército Brasileiro (EB) e pela Secretaria do Patrimônio da União (SPU) de acordo com os critérios da NBR 14653 e da Instrução Normativa (IN) vigente. Elas são de acesso restrito; não se encontram, portanto, disponíveis neste repositório.

Os _scripts_ foram implementados no Google Colaboratory (Colab) em linguagem de programação _Python_ e estão organizados da seguinte forma:

0. Enriquecimento das bases de dados com quantitativos de equipamentos urbanos e de estabelecimentos comerciais em raio de 400 metros de cada imóvel por meio de API Google Places Nearby Search. (arquivo "0_requisicoes_gcp.ipynb")
1. Análise gráfica e seleção de atributos. (arquivo "1_analise_grafica_selecao_atributos.ipynb")
2. Resumo das abordagens com eliminação de _outliers_ e com transformação de variáveis. (arquivo "2_resumo_abordagens.ipynb")
3. Modelos urbanos de regressão linear múltipla (OLS) e espacial (S2SLS). (arquivo "3_ols_s2sls_urbanos.ipynb")
4. Modelos urbanos lineares de aprendizagem de máquina (_SGDRegressor_). (arquivo "4_sgdregressor.ipynb")
5. Modelos de rede neural artificial não linear (_MLPRegressor_). (arquivo "5_mlpregressor.ipynb")
6. Modelos _ensemble_ não lineares (_XGBRegressor_). (arquivo "6_xgbregressor.ipynb")
7. Modelos rurais de regressão linear múltipla (OLS) e espacial (S2SLS). (arquivo "7_ols_s2sls_rurais.ipynb")  
