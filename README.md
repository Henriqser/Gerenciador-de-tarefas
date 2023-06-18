# Gerenciador de Tarefas

Este é um programa simples em Python para gerenciar tarefas. Ele permite criar, visualizar, atualizar, remover e filtrar tarefas. As tarefas são armazenadas em um arquivo JSON para persistência de dados.

## Pré-requisitos

Antes de executar o programa, certifique-se de ter instalado o Python em seu sistema. Além disso, é necessário instalar a biblioteca `colorama`. Você pode instalar a biblioteca executando o seguinte comando:

```
pip install colorama
```

## Como usar

1. Baixe o código-fonte do programa.

2. Certifique-se de que o arquivo `tarefas.json` esteja presente no mesmo diretório do código.

3. Abra um terminal ou prompt de comando e navegue até o diretório onde o código está localizado.

4. Execute o seguinte comando para iniciar o programa:

```
python nome_do_arquivo.py
```

5. O menu principal será exibido com as opções disponíveis. Use os números correspondentes às opções para interagir com o programa.

6. Quando terminar de usar o programa, você pode sair selecionando a opção "0" no menu. As tarefas serão salvas automaticamente no arquivo `tarefas.json`.

## Funcionalidades

### Carregar Tarefas

A função `carregar_tarefas` é responsável por ler o arquivo `tarefas.json` e retornar as tarefas armazenadas nele. Caso o arquivo não exista, uma lista vazia será retornada.

### Salvar Tarefas

A função `salvar_tarefas` é responsável por salvar as tarefas no arquivo `tarefas.json`. Ela recebe como parâmetro a lista de tarefas e escreve no arquivo no formato JSON.

### Exibir Menu

A função `exibir_menu` exibe o menu principal do programa, mostrando as opções disponíveis para o usuário.

### Criar Tarefa

A função `criar_tarefa` solicita ao usuário que digite o título, a descrição e o status da nova tarefa. Em seguida, ela retorna um dicionário contendo os dados da tarefa.

### Visualizar Tarefas

A função `visualizar_tarefas` recebe como parâmetro a lista de tarefas e exibe todas as tarefas na saída padrão. Se não houver tarefas, uma mensagem informando que nenhuma tarefa foi encontrada será exibida.

### Atualizar Tarefa

A função `atualizar_tarefa` permite atualizar uma tarefa existente. Ela exibe as tarefas disponíveis e solicita ao usuário o número da tarefa que deseja atualizar. Em seguida, o usuário pode fornecer um novo título, descrição e status para a tarefa selecionada.

### Remover Tarefa

A função `remover_tarefa` permite remover uma tarefa existente. Ela exibe as tarefas disponíveis e solicita ao usuário o número da tarefa que deseja remover. A tarefa selecionada será removida da lista de tarefas.

### Filtrar Tarefas

A função `filtrar_tarefas` permite filtrar as tarefas por status. O usuário deve digitar o status pelo qual deseja filtrar as tarefas. Em seguida, serão exibidas apenas as tarefas que possuem o status informado.

## Considerações Finais

Este programa simples de gerenciamento de tarefas pode ser uma ótima base para criar aplicações mais avançadas. Sinta-se à vontade para modificar e melhorar o código de acordo com suas necessidades. Espero que seja útil e ajude você a gerenciar suas tarefas de forma eficiente!
