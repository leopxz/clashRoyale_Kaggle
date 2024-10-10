# Clash Royale Battle Analysis API

## Descrição
Esta aplicação é uma API construída com Flask e MongoDB Atlas que analisa dados de batalhas e cartas do jogo Clash Royale. A API permite executar consultas sobre as batalhas, como a porcentagem de vitórias/derrotas de uma carta em um determinado período, decks com maior percentual de vitórias e o número de derrotas em batalhas usando uma combinação específica de cartas.

## Funcionalidades
Obter porcentagem de vitórias/derrotas para uma carta: Calcula a taxa de vitórias ou derrotas para uma carta específica em um intervalo de tempo.
Consultar decks com alto percentual de vitórias: Retorna os decks que têm uma porcentagem de vitórias acima de um determinado valor.
Número de derrotas com combinação de cartas: Informa o número de derrotas em batalhas que envolveram uma combinação específica de cartas em um intervalo de tempo.

## Tecnologias Utilizadas
Flask: Framework web para Python usado para construir a API.
MongoDB Atlas: Banco de dados NoSQL para armazenar os dados de batalhas e jogadores.
MongoEngine: ODM (Object-Document Mapper) usado para modelar os documentos do MongoDB em objetos Python.

## Instalação
Clone o repositório:
```
git clone https://github.com/leopxz/clashRoyale_Kaggle
```
Navegue até o diretório do projeto:
```
cd clashRoyale_Kaggle
```
Instale as dependências:
```
pip install -r requirements.txt
```
Configure o arquivo .env com suas credenciais do MongoDB Compass e outras variáveis de ambiente.

## Execução
Inicie o servidor Flask:
```
python app.py
```
Acesse a API no navegador:
```
http://127.0.0.1:5000
```

## Endpoints

### GET /win-loss-percentage
Retorna a porcentagem de vitórias ou derrotas para uma carta específica em um intervalo de tempo.

Parâmetros de Query:

cardId (obrigatório): ID da carta
startTime (obrigatório): Data e hora de início do intervalo
endTime (obrigatório): Data e hora de fim do intervalo

### POST /winning-decks
Retorna decks com uma porcentagem de vitórias maior que um valor especificado.

Body JSON:

percentage (obrigatório): Percentual de vitórias mínimo
startTime (obrigatório): Data e hora de início do intervalo
endTime (obrigatório): Data e hora de fim do intervalo

### POST /losses-for-combo
Calcula o número de derrotas em batalhas envolvendo uma combinação específica de cartas.

Body JSON:

cardIds (obrigatório): Lista de IDs de cartas
startTime (obrigatório): Data e hora de início do intervalo
endTime (obrigatório): Data e hora de fim do intervalo

## Estrutura do Projeto
<br>
ClashRoyale/<br>
│<br>
├── app.py  # Arquivo principal para inicializar o Flask e configurar as rotas<br>
├── requirements.txt  # Dependências do projeto (caso não tenha, é importante adicionar)<br>
│<br>
├── Controller/<br>
│   ├── battle_controller.py<br>
│   └── troop_controller.py<br>
│<br>
├── DTOs/<br>
│   ├── battle_dto.py<br>
│   └── troop_dto.py<br>
│<br>
├── Documents/  # Modelos específicos para o MongoDB (MongoEngine Documents)<br>
│   ├── battle.py<br>
│   ├── card.py<br>
│   ├── cards.py<br>
│   ├── clan.py<br>
│   ├── player.py<br>
│   ├── structure.py<br>
│   ├── team.py<br>
│   ├── total_card.py<br>
│   └── troop.py<br>
│<br>
├── Mapper/  # Responsável por conversões entre DTOs e Models/Documents<br>
│   └── battle_mapper.py<br>
│<br>
├── Models/  # Modelos mais genéricos, não atrelados diretamente ao MongoDB<br>
│   ├── battle.py<br>
│   ├── deck.py<br>
│   └── player.py<br>
│<br>
├── Repository/  # Camada responsável por interagir diretamente com o banco de dados<br>
│   ├── battle_repository.py<br>
│   └── troop_repository.py<br>
│<br>
├── Services/  # Regras de negócio e lógica do sistema<br>
│   ├── battle_service.py<br>
│   └── troop_service.py<br>
│<br>
├── static/  # Arquivos estáticos (CSS, JS, imagens, etc.)<br>
│   └── css/<br>
│       └── style.css<br>
│<br>
└── templates/  # Templates HTML para renderização<br>
    ├── battle.html<br>
    ├── index.html<br>
    ├── players.html<br>
    └── troop.html<br>
