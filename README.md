# Previsão de gênero literário através de Machine Learning e NLP
O foco desse projeto é criar um modelo de Machine Learning (ML) que possa prever o gênero literário de um livro através de uma breve descrição da obra.
Foram utilizadas técnicas de Natural language processing (NLP), como term frequency-inverse document frequency com unigramas e bigramas, além de técnicas de Machine Learning para que o modelo possa ser usado em um problema de multilabel (onde o resultado pode ter várias classes ao invés de uma só), que nesse caso foi one-vs-rest.

## Ferramentas usadas
- Numpy
- Pandas
- NLTK
- Scikit-learn
- Regex

## Próximos passos
- Adicionar e avaliar outros modelos de ML;
- Adicionar hiperparametrização nos modelos para obter resultados melhores;
- Usar um dataset maior, tendo em vista que esse possuía cerca de 1300 livros;
