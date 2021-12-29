# 🟢 Avaliação Sprint 4 - Programa de Bolsas Compass.uol e UFMS 🟢 

Quarta sprint do programa de bolsas Compass.uol para formação em chatbot Rasa.

---

## 🤖 ChatBot 
O chatbot construído tem como objetivo criar uma conversa com o usuário onde ele pode realizar uma consulta com base na [API](https://openweathermap.org/current) para visualizar a temperatura de uma determinada cidade no planeta, agora com o banco de dados funcional, é possível armazenar as  buscas que o usuário faz durante sua conversa com o bot.

---

# 🔨 Desenvolvimento
## 📚 Bibliotecas utilizadas 
* [Action](https://rasa.com/docs/rasa/actions/)
* [Tracker](https://rasa.com/docs/action-server/sdk-tracker/)
* [SlotSet](https://rasa.com/docs/action-server/sdk-events/)
* [CollectingDispatcher](https://rasa.com/docs/action-server/sdk-dispatcher/)
* [PyMongo](https://pymongo.readthedocs.io/en/stable/)
* [MongoClient](https://mongodb.github.io/node-mongodb-native/api-generated/mongoclient.html)
  
---

## Dependências
* Rasa 3.0
* Python 3.8
* Pymongo 3.10.1 
* MongoDB
* Docker
  
---

## 🤖 Utilizando o Rasa ChatBot com MongoDB

1. Faça a clonagem deste repositório em sua máquina.
   
2. No seu terminal de preferência, execute os comandos abaixo:
   
```
rasa train

rasa run actions

rasa shell
```
Com a aplicação rodando, siga o seguinte fluxo:

* Dê os cumprimentos ao chatbot
* Informe sua intensão
* Informe seu nome
* Informe a cidade que deseja conferir a temperatura
---

## 🐳 Docker

A aplicação não está funcionando corretamente com docker-compose, um problema no arquivo persiste até agora. Mas assim que for solucionado bastará ao usuário digitar "docker-compose run -u " root" rasa" no console de preferência e a aplicação estará funcional, sem o uso dos outros comandos.

## Desenvolvido por 
- 👨‍💻 Leonardo Oliveira
---