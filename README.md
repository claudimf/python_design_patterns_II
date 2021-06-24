# Design Patterns Python II

👋 Olá, Seja Bem-vindo(a) ao 'Design Patterns Python II: Boas práticas de programação'.

# Projeto 'Design Patterns Python I: Boas práticas de programação' do curso:

## [Design Patterns Python II: Boas práticas de programação](https://cursos.alura.com.br/course/design-patterns-python-2)

# Aulas

<details>
    <summary>Fábricas e o problema de criação de objetos</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>Fábricas e o problema de criação de objetos</li>
        <li>Nomenclatura</li>
        <li>Factory e Builder</li>
        <li>Factory sem classe</li>
        <li>Escrevendo a fábrica</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Salvando estados anteriores e o Memento</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>Salvando estados anteriores e o Memento</li>
        <li>Criando a classe Contrato</li>
        <li>Memento</li>
        <li>Necessidade da Classe Estado</li>
        <li>Problemas do memento</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>DSLs e o Interpreter</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>DSLs e o Interpreter</li>
        <li>Quando usar?</li>
        <li>Interpreter</li>
        <li>Classe abstrata</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Estruturas de dados e o Visitor</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>Estruturas de dados e o Visitor</li>
        <li>Implementando o padrão Visitor</li>
        <li>Outra implementação de visitor</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Diferentes ações com Command</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>Diferentes ações com Command</li>
        <li>Classe pedido</li>
        <li>Diferenças</li>
        <li>Command</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

# Notas das aulas:

## Factory
Para executar um script python, faça conforme o exemplo abaixo:
```sh
docker-compose run --rm app python 01_Factory/conectar_banco.py
```

# Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

## Listar pacotes:
```sh
docker-compose run --rm app pipdeptree
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm app bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

## Configurar o banco:
```sh
1° [dentro do container] - Subir o banco:
docker-compose up -d db

2° [dentro do container] - Listar container:
docker ps

3° [dentro do container] - Entrar no container:
docker exec -it [id do db] bash

5° [dentro do container] - Entrar no banco e rodar as seeds:
mysql -uroot -psecret alura < docker-entrypoint-initdb.d/db_seed.sql

6° [dentro do container] - Sair de dentro do banco de desenvolvimento:
 CRTL + D
```

## Acessar o banco:
```sh
1° [dentro do container] - Subir o banco:
docker-compose up -d db

2° [dentro do container] - Listar container:
docker ps

3° [dentro do container] - Entrar no container:
docker exec -it [id do db] bash

5° [dentro do container] - Entrar no banco:
mysql -u root -psecret alura

6° [dentro do container] - Sair de dentro do banco de desenvolvimento:
 CRTL + D
```

# Referências utilizadas

[1° Conteinerização de scripts em Python](https://github.com/claudimf/containerized_python)

[2° Awesome Compose](https://github.com/docker/awesome-compose)

[3° Docker Compose MySql Database Seed](https://onexlab-io.medium.com/docker-compose-mysql-database-seed-3bcbdfc51e8b)

[4° Connecting to MySQL Using Connector/Python](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)

[5° Handy MySQL Commands](http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm)

[6° Factory Method](https://refactoring.guru/pt-br/design-patterns/factory-method)

[7° Memento](https://refactoring.guru/pt-br/design-patterns/memento)

[8° Interpreter](https://blog.matheuscastiglioni.com.br/interpreter-padroes-de-projeto-em-java/#:~:text=Conhecendo%20o%20padr%C3%A3o%20Interpreter,interpretar%20DSL's%20ou%20criar%20compiladores.)

[9° Visitor](https://refactoring.guru/pt-br/design-patterns/visitor)

[10° Command](https://refactoring.guru/pt-br/design-patterns/command)