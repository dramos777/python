## Comandos Python3
A opção **-c** permite executar comandos no terminal.

### print

```
python -c "print(56 - 6)"
python -c "print('Teste')"
python -c "print('teste'.upper())"
```
## Modulos Python
A opão **-m** faz chamada de modulos.

### site
O módulo **site** exibe como o python está instalado, o caminho de onde os python vai buscar pacotes)
```
python -m site
```
### turtledemo
Se o Python tiver sido instalado com suporte a este pacote ele abrirá uma interface gráfica com alguns exemplos de jogos e animações para se basear
```
python -m turtledemo
```
### pip
O pip é um modulo utilizado para instalar pacotes python. Exemplo de instalação com o pacote ipython
```
python -m pip install ipython
```
Para atualizar o pip:
```
python -m pip install --upgrade pip
```

## Código Python3 e boas práticas
Para evitar conflitos com a versão do python rodando no sistema operacional é recomendado criar um ambiente virtual para instalar as dependências do código que será criado. Os diretórios exibidos pelo módulo **site** são os diretórios onde o python está instalado. Para criar o ambiente virtual utilizamos o módulo **venv** que por sua vez adiciona os diretórios da instalação do python. É considerado boa prática criar o ambiente virtual com o nome **.venv** e incluído este arquivo no **.gitignore**.

```
python3 -m venv .venv
```
O pacote python3-venv precisa estar instalado na máquina
```
apt install python3-venv
```
Não basta apenas criar o ambiente, é necessário realizar a ativação para garantir que o python utilizado seja o do ambiente virtual e não o do sistema operacional. Isso é feito carregando o arquivo .venv/bin/active. Ex:
``` 
source .venv/bin/activate
```
Após o ambiente ser carregado tudo que for alterado ou adicionado no python afetará o python do ambiente virtual e não o python instalado no sistema operacional

## ipython
Assim como o comando python, o ipython (se instaldo) abre um terminal, a diferença é que a aparência é melhor e tem mais opções

# A importância dos tipos de dados
Para fazer um bom código é necessário entender bem os tipos de dados

- classe, categoria, tipo são uma coisa só em python, estão relacionadas. Hora ouvirá alguém chamar classe, hora categoria e hora tipo

Os tipos de dados estão classificados em duas categorias:
- Tipo de dados primário (Scalar Types)
- Tipo de dados compostos

# Tipo de dados primário (Scalar Types)
Representa um único valor. Ex: numero = 65

Tipos (classes):
- int
```
dir(int)
```
 
# Formatação de Textos
O python é conhecido por ser uma linguagem dinâmica de tipagem forte, ou seja, ele precisa permitir que os tipos são compatíveis para executar, caso contrário exibe um erro na tela sem tentar resolver.

Site para consulta de tipos de formatação: https://pyformat.info

### Formatação - método concatenação
Na concatenação o texto com as variáveis são imprressos direto na tela utilizando as ""
```
#VARIABLES
nome = "João"
saldo = 30.0

#O exemplo abaixo exibe um erro pois não é possível concatenar string com float
"O saldo do " + nome + " é total de " + saldo

#Para garantir que os tipos sejam compatíveis é preciso fazer a conversão
"O saldo do " + nome + " é total de " + str(saldo)
```
### Formatação - método interpolação (old style)
Na interpolação nós criamos um template com o texto e os placeholders (marcações no texto)

Exemplo 1
```
#VARIBALES
nome = "João"
saldo = 30.0

#Template com placeholders declarados (%s string, %f float)
template = "O saldo do %s é o total de %f"

#EXECUTION
template % (nome, saldo)
```
Exemplo 2
```
#Template (%s = string, %03d = 3 digitos, %.3f = 3 digitos float)
msg = "Olá, %s você é o player n %03d e você tem %.3f pontos"

#EXECUTION
msg % ("João", 2, 987.3)
```
Exemplo 3
```
email_tmpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
Este produto é ótimo para resolver
%(texto)s
Clique agora em %(link)s
Apenas %(quantidade)d disponíveis
Preço promocional %(preco).2f
"""

clientes = ["Maria","João","Bruno"]
for cliente in clientes:
    print(
        email_tmpl
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
           }
         )
```
### Formatação - método str.format (new style)
O método str.format permite a formatação do texto de diversas maneiras como: centralizado, alinhado à esquerda/direita.
Exemplo 1
```
#Template
msg = "Olá, {} você é o player n {} e você tem {} pontos"

#EXECUTION
msg.format("João", 2, 987.3)
```
Exemplo 2
```
#Template (:03d = 3 digitos, :.3f = 3 digitos float)
msg = "Olá, {} você é o player n {:03d} e você tem {:.3f} pontos"

#EXECUTION
msg.format("João", 2, 987.3)
```
Exemplo 3
```
#Template (:03d = 3 digitos, :.3f = 3 digitos float)
msg = "Olá, {nome} você é o player n {numero:03d} e você tem {pontos:.3f} pontos"

#EXECUTION
msg.format(nome="João", numero=2, pontos=987.3)

#OBS.: utilizando tags não importa a ordem que for declarada na execução. Exemplo:
msg.format(pontos=987.3, nome="João", numero=2)
```
Exemplo 4
```
#Formatado com o texto no centro com base de 20 caracteres
"{:^20}".format("João")

#Formatado com o texto à esquerda com base de 20 caracteres
"{:<20}".format("João")

#Formatado com o texto à direita com base de 20 caracteres
"{:>20}".format("João")

#Formatado com o texto no centro com base de 20 caracteres e preencher os espaços com "#"
"{:#^20}".format("João")
```
### Formatação - método f-strings (new style)
Implementado a partir do python 3. O método f-strings obrigatoriamente precisa ter uma string após o **f** e uma variável válida.
syntax: f"string"{variavelDeclarada}

Exemplo 1
```
#VARIABLES
nome = "João"

#EXECUTION
f"Olá, {nome}"
```
Exemplo 2
```
#VARIABLES
nome = "João"
saldo = 90

#EXECUTION
f"Olá {nome} você tem {saldo} na conta"
```
Exemplo 3
```
#VARIABLES
nome = "João"
saldo = 90.3

#EXECUTION
f"Olá {nome} você tem {saldo:.2f} na conta"
```
### Casos de uso
- concatenação (%s) - é ultil quando estiver utilizando a biblioteca **logging**

- str.format {} - é indicado para mensagens longas

- f-strings - utilizada para o restante (msg, print, erro, etc)

# Tipo de dados composto
Representa vários valores em um único objeto.

### Tuple (tuplas) - type: sequence
- Lida a partir da posição 0
- Os dados são armazenados no mesmo objeto e é identificado associando  o ID e a posição de memória. Ex:

|cores          |
|---------------|
|0       ID(1)  |
|---------------|
|1       ID(2)  |
|---------------|
|2       ID(3)  |
|---------------|
|type: sequence |
