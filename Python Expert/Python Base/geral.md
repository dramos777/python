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
Para atualizaro o pip:
```
python -m pip install --upgrade pip
```

## Código Python3 e boas práticas
Para evitar conflitos com a versão do python rodando no sistema operacional é recomendado criar um ambiente virtual para instalar as dependências do código que será criado. O módulo site exibe os diretórios onde o python está instalado e o módulo venv cria o ambiente virtual adicionando esses diretórios nele. É considerado boa prática criar o ambiente virtual com o nome .venv

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
Após o ambiente ser carregado tudo que for alterado ou adicionado no python afetará o python do ambiente virtual e não so sistema operacional

## ipython
Assim como o comando python, o ipython (se instaldo) abre um terminal, a diferença é que a aparência é melhor e tem mais opções
