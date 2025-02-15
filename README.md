Ola! deixarei aqui a explicação da resolução dos exercicios propostos!

Obs: Inicialmente resolvi as questões criando algoritmos sem modularização, e depois realizei a modularização de cada um, o Docker esta funcionando apenas para a questão 3 modularizada e há uma pasta com as soluções sem modularização.

Questão 2 : para realizar a leitura da tabela CSV utilizei a biblioteca pandas, depois armazenei essa tabela dentro de um DataFrame
para poder manibular os dados da tabela e conseguir chegar a solução necessaria, para conseguir chegar ao faturamento maximo e o faturamento minimo, eu utilizei novamente o pandas
desta vez fiz uso das funçõs idxmax e idxmin que fazem a leitura de um indice de valor maximo e minimo de um Dataframe ou Series.

Questão 3: na resolução desta questão, utilizei o jsonify de Flask para transformar nossos dados python em JSON, fiz a utilização do Blueprint para me ajudar com a modularização do código, fiz a requisição dos numeros para devolver um Json
com a resposta, e adicionei condicionais para que o numero digitado não fosse inválido ou não fosse digitado! caso seja digitado corretamente, ele devolve o resultado da soma.

Questão 4: para a questão 4, utilizei de Asyncio e time para realizar a minha programação assíncrona, criei uma pequena função para aguardar a execução simultanea das tarefas e printei na tela, por fim mostrei as operações com exito e 
o tempo de execução delas!

Questão 7: nesta questão fiz a utilização de werkzeug para manipulação de senha de forma segura, flash_limiter para criar um limitador de tentativas e por fim, retirei de app.run() o Debug=true, e essa tarefa foi realizada para 
evitar um possivel vazamento de dados!
