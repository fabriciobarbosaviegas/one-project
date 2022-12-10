# The One Project
 The One project has a purpose of making a unified messenger to communicate with all message systems (or most of them), is part of my final project to complete Harvard CS50.
 
 [Read in Portuguese](#pt-br)

## Index
1. Modification in progress
2. The technologies used
    - Technologies
3. About the Matrix protocol
4. Bridges, the hearth of the One

## Modification in progress
- [ ] Create a Matrix client
- [ ] Establish communication between client and server
- [ ] Establish a bridge between any Messenger
- [ ] Communicate via text with any Messenger
- [ ] Establish a bridge between the other Messengers

  - [ ] WhatsApp
  - [ ] Telegram
  - [ ] Linkedin
  - [ ] Messenger
  - [ ] Instagram Direct
  - [ ] Twitter Direct

## The technologies used
 As part of the requirements for this project to go through the course, I need to use at least one technology learned within it, so, as a rule, the backend needs to be developed in flask, however limiting this may be, in the future, if you want to continue with the project, I plan to migrate it to django.
 
### Technologies:
[![Python](https://img.shields.io/badge/-Python-000?&logo=python)](https://github.com/fabriciobarbosaviegas?tab=repositories&q=&type=&language=python)
[![Flask](https://img.shields.io/badge/-Flask-000?&logo=flask)](https://github.com/fabriciobarbosaviegas?tab=repositories&q=&type=&language=python)
[![HTML](https://img.shields.io/badge/-HTML-000?&logo=html5&logoColor=orange)](https://github.com/fabriciobarbosaviegas?tab=repositories&q=&type=&language=html)
[![CSS](https://img.shields.io/badge/-CSS-000?&logo=css3&logoColor=blue)](https://github.com/fabriciobarbosaviegas?tab=repositories&q=&type=&language=css)
[![JavaScript](https://img.shields.io/badge/-JavaScript-000?&logo=JavaScript&logoColor=ddc508)](https://github.com/fabriciobarbosaviegas?tab=repositories&q=&type=&language=javascript)
[![Matrix](https://img.shields.io/badge/-Matrix-000?&logo=Matrix&logoColor=fff)](#sobre-o-protocolo-matrix)

## About the Matrix protocol
Matrix is really a decentralised conversation store rather than a messaging protocol. When you send a message in Matrix, it is replicated over all the servers whose users are participating in a given conversation - similarly to how commits are replicated between Git repositories. There is no single point of control or failure in a Matrix conversation which spans multiple servers: the act of communication with someone elsewhere in Matrix shares ownership of the conversation equally with them. Even if your server goes offline, the conversation can continue uninterrupted elsewhere until it returns. [Read more](https://matrix.org/)

## Bridges, the hearth of the One
An important idea in Matrix is interoperability. This means that Matrix is open to exchange data and messages with other platforms using an Open Standard. Thanks to this, you can connect to any shipment independently, which is a fundamental concept for it to work. We call these connections to other platforms bridges. The Matrix core team maintains bridges to Slack, IRC, XMPP and Gitter, and meanwhile the wider Matrix community provides bridges to Telegram, Discord, WhatsApp, Facebook, Hangouts, Signal and more. [Read more](https://matrix.org/bridges)

# PT-BR

## O projeto One
O projeto One tem como proposta criar um messenger unificado para comunicar com todos os sistemas de mensagem (ou a maioria deles), sendo parte do meu final project para completar o CS50 de Harvard.

## Indices
1. Modificações em progresso
2. As tecnologias utilizadas
    - Tecnologias
3. Sobre o protocolo Matrix
4. Pontes, o coração do One

## Modificações em progresso

- [ ] Criar um client Matrix
- [ ] Estabelecer comunicação entre client e server
- [ ] Estabelecer uma ponte entre qualquer Messenger
- [ ] Comunicar via texto com qualquer Messenger
- [ ] Estabelecer ponte entre os demais Messengers

  - [ ] WhatsApp
  - [ ] Telegram
  - [ ] Linkedin
  - [ ] Messenger
  - [ ] Instagram Direct
  - [ ] Twitter Direct

 ## As tecnologias utilizadas
 Como parte das exigências para que este projeto seja pelo curso necessito utilizar pelo menos uma tecnoligia aprendida dentro dele, assim, via de regra o backend necessita ser desenvolvido em flask, por mais limitante que isso seja, futuramente, caso queira seguir com o projeto, planejo migra-lo para django.
 
 ### Tecnologias:
[![Python](https://img.shields.io/badge/-Python-000?&logo=python)](https://github.com/fabriciobarbosaviegas?tab=repositories&q=&type=&language=python)
[![Flask](https://img.shields.io/badge/-Flask-000?&logo=flask)](https://github.com/fabriciobarbosaviegas?tab=repositories&q=&type=&language=python)
[![HTML](https://img.shields.io/badge/-HTML-000?&logo=html5&logoColor=orange)](https://github.com/fabriciobarbosaviegas?tab=repositories&q=&type=&language=html)
[![CSS](https://img.shields.io/badge/-CSS-000?&logo=css3&logoColor=blue)](https://github.com/fabriciobarbosaviegas?tab=repositories&q=&type=&language=css)
[![JavaScript](https://img.shields.io/badge/-JavaScript-000?&logo=JavaScript&logoColor=ddc508)](https://github.com/fabriciobarbosaviegas?tab=repositories&q=&type=&language=javascript)
[![Matrix](https://img.shields.io/badge/-Matrix-000?&logo=Matrix&logoColor=fff)](#sobre-o-protocolo-matrix)

 ## Sobre o protocolo Matrix
 Matrix é um armazenamento de conversação descentralizado, em vez de um protocolo de mensagens. Quando você envia uma mensagem no Matrix, ela é replicada em todos os servidores cujos usuários estão participando de uma determinada conversa - da mesma forma que os commits são replicados entre repositórios Git. Não há um único ponto de controle ou falha em uma conversa da Matrix que abrange vários servidores: o ato de comunicação com alguém em outro lugar na Matrix compartilha a propriedade da conversa igualmente com eles. Mesmo que seu servidor fique offline, a conversa pode continuar ininterrupta em outro lugar até que ela retorne. [Leia mais](https://matrix.org/)

## Pontes, o coração do One
Uma ideia importante em Matrix é a interoperabilidade. Isso significa que a Matrix está aberta para troca de dados e mensagens com outras plataformas usando um Padrão Aberto. Graças a isso o One pode conectar-se a qualquer mensageiro de modo independente sendo esse um conceito fundamental para que ele funcione. Chamamos essas conexões com outras plataformas de pontes. A equipe principal do Matrix mantém pontes para Slack, IRC, XMPP e Gitter e, enquanto isso, a comunidade Matrix mais ampla fornece pontes para Telegram, Discord, WhatsApp, Facebook, Hangouts, Signal e muito mais. [Leia mais](https://matrix.org/bridges/)
