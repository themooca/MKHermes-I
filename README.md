# MKHermes-I

  - O MKHermes-I é um bot feito em python usando a biblioteca do selenium com o objetivo de spammar mensagens no WhatApp em grande escala. O MKHermes-I teve como base o WhatsApp Bot Selenium (https://github.com/harshitsidhwa/WhatsApp-bot-selenium), porém o codigo original é bem... quebrado. Ele não estava funcionando (pelo menos comigo) e só mandava mensagem pra meia dúzia de pessoas, agora o MKHermes-I funciona pra muitos contatos.

# Funções!

  - Manda mensagens para múltiplos contatos
  - Utiliza Tabelas em XLSX para pegar os contatos
  - Pode enviar múltiplas mensagens para os contatos
  
### Pré-requisitos

* [Linux](https://manjaro.org/) - Eu não testei em Windows e Mac, então não sei como funciona lá.
* [Python 3+](https://www.python.org/download/releases/3.0/?) - Pyhton 3.6+ verion
* [Selenium](https://github.com/SeleniumHQ/selenium) – Biblioteca de automação para navegadores
* [openpyxl](https://pypi.org/project/openpyxl/) - Para ler os XLSX

### Tutorial

O Tutorial esta sendo feito em Arch Linux, porem da pra fazer na sua distribuição favorita, basta tem um conhecimento basico.
Passo 1: Instale o Python e o Selenium

```sh
$ sudo pacman -S python
```

Passo 2: Instale o Chromium
```sh
$ sudo pacman -S chromium
```

Passo 3: Vamos copiar o repositório do git e entre no diretório
```sh
$ git https://github.com/themooca/MKHermes-I
$ cd MKHermes-I
```
Passo 4: Vamos criar um ambiente virtual e pegar os pré-requisitos
```sh 
$ python – m venv venv
$ source venv/bin/activate
$ pip3 install selenium
$ pip3 install openpyxl
```
Passo 5: Modifique o ‘contatos.xlsm’ e modifique a mensagem dentro do MKHermes-I.py com algum editor de texto.

Passo 6: Inicie o arquivo com
```sh
python	MKHermes-I.py
```

Passo 7: Escaneie o QR code e pressione enter no terminal
Pronto, já esta rodando.

### Nota
A criterio de curiosidade, Hermes na mitologia grega era o mensageiro dos deuses, por isso aqui esta.

Agradeço ao Eduardo Mendes que me ajudou nos primeiros passos do python e do selenium, e aqui esta meu primeiro codigo. Segue o link do curso dele (https://www.youtube.com/playlist?list=PLOQgLBuj2-3LqnMYKZZgzeC7CKCPF375B).


