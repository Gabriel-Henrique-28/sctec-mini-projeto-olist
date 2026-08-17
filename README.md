
Readme · MD
# sctec-mini-projeto-olist
 
## Objetivo do Projeto
 
A Olist precisa dos dados de suas milhares de transações diárias para alimentar seus modelos de Business Intelligence (BI) e seus modelos preditivos de Machine Learning. Porém, ela não pode injetar esses dados crus diretamente nesses modelos — e é justamente esse problema que este projeto busca resolver.
 
Este projeto contém um script que lê os dados de transações da Olist, realiza a limpeza e sanitização desses dados e retorna um mini relatório sobre o processamento realizado.
 
## Pré-requisitos
 
- Python instalado.
## Como Executar
 
1. Crie uma pasta chamada `data` no diretório raiz do projeto.
2. Insira os arquivos `.csv` que serão lidos pelo script dentro da pasta.
3. Execute o comando abaixo no terminal:
```bash
python main.py
```
 
## Reflexão Teórica sobre Machine Learning
 
Dados são a parte mais importante do qualquer modelo de machine learning, por isso que existe a regra "garbage in, garbage out" (entra lixo, sai lixo), isso significa que se um modelo for treinado com dados ruins, o resultado dele será ruim, por isso que a limpeza dos dados é uma das etapas mais importantes ao treinar um modelo de machine learning.

Um dos princípais problemas que a limpeza de dados ajuda a resolver é o overfitting, mesmo a maior parte da causa de um overfitting ser um modelo complexo demais para os dados utilizados, uma boa limpeza de dados pode ajudar a diminuir drasticamente esse problema, pois a limpeza dos dados ira diminuir o ruido na aprendizagem do modelo, por exemplo: excluir outliers impede do modelo tratar exceções como padrões, padronizar categorias evita o modelo tratar categorias que seriam iguais como diferentes (ex: "Categoria" e "categoria"), tratar nulos e vazios para que tenham um valor único padrão sendo média, mediana ou até 0 dependendo do contexto do projeto (ex: " ", "" e null) impede que o modelo aprenda padrões diferentes para uma única informação. Quanto mais os dados forem limpos e polidos menor será o ruido na aprendizagem do modelo e melhor ele performara.