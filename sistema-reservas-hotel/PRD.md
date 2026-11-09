# PRD — Sistema Web de Reservas de Hotel

## 1. Visão geral

O Sistema Web de Reservas de Hotel tem como objetivo permitir o cadastro de hóspedes, consulta de quartos disponíveis e gerenciamento de reservas de hospedagem.

A aplicação permitirá que usuários realizem reservas por meio de uma interface web, com validação dos dados, verificação de disponibilidade e cálculo automático do valor total da hospedagem.

O sistema será desenvolvido em Python utilizando FastAPI, Pydantic e páginas HTML renderizadas com Jinja2.

## 2. Objetivos

- Permitir o cadastro e consulta de hóspedes.
- Disponibilizar informações sobre os quartos do hotel.
- Consultar a disponibilidade de quartos em determinado período.
- Criar, consultar e cancelar reservas.
- Validar os dados informados pelos usuários.
- Calcular automaticamente o valor das hospedagens.
- Aplicar cupons promocionais.
- Simular o envio de e-mails de confirmação.

## 3. Funcionalidades

### F01 — Cadastro de hóspedes

Permitir o cadastro de hóspedes contendo:

- Nome completo.
- E-mail.
- Telefone.
- Documento de identificação.

Os campos deverão ser validados antes do cadastro.

### F02 — Consulta de quartos

Disponibilizar informações sobre os quartos, incluindo:

- Identificador do quarto.
- Categoria.
- Capacidade máxima.
- Valor da diária.

Categorias disponíveis:

| Categoria | Capacidade | Diária |
|---|---:|---:|
| Standard | 2 pessoas | R$ 200,00 |
| Luxo | 3 pessoas | R$ 350,00 |
| Suíte | 4 pessoas | R$ 500,00 |

### F03 — Consulta de disponibilidade

Permitir a consulta de quartos disponíveis considerando:

- Data de check-in.
- Data de check-out.
- Quantidade de adultos.
- Quantidade de crianças.

O sistema deverá considerar a capacidade do quarto e as reservas existentes.

### F04 — Criação de reservas

Permitir que um hóspede realize uma reserva informando:

- Identificação do hóspede.
- Tipo de quarto desejado.
- Quantidade de adultos.
- Quantidade de crianças.
- Data de check-in.
- Data de check-out.
- Cupom promocional opcional.

O sistema deverá validar as informações, verificar a disponibilidade e calcular o valor total.

### F05 — Consulta de reservas

Permitir a listagem das reservas cadastradas e a consulta individual de seus detalhes.

### F06 — Cancelamento de reservas

Permitir o cancelamento de uma reserva existente.

Reservas canceladas não deverão continuar ocupando a disponibilidade do quarto.

### F07 — Confirmação por e-mail

Após a criação de uma reserva, o sistema deverá acionar um serviço responsável pelo envio de uma confirmação por e-mail.

O serviço será simulado, sem envio de mensagens reais.

Uma falha no serviço de e-mail deverá ser tratada sem comprometer o registro da reserva.

## 4. Regras de negócio

### RN01 — Quantidade mínima de adultos

Uma reserva deve possuir pelo menos 1 adulto.

- Valores inferiores a 1 são inválidos.
- Valores iguais ou superiores a 1 são válidos, respeitando a capacidade do quarto.

### RN02 — Quantidade de crianças

A reserva pode possuir de 0 a 4 crianças.

- 0 crianças é válido.
- Valores entre 1 e 4 são válidos.
- Valores negativos são inválidos.
- Valores superiores a 4 são inválidos.

### RN03 — Quantidade de noites

A hospedagem deve possuir entre 1 e 30 noites.

- 0 noites é inválido.
- Valores entre 1 e 30 são válidos.
- Valores superiores a 30 são inválidos.

A quantidade de noites será calculada automaticamente pela diferença entre as datas de check-in e check-out.

### RN04 — Tipo de quarto

Os tipos de quarto disponíveis são:

- standard.
- luxo.
- suite.

Qualquer outro tipo deverá ser rejeitado.

### RN05 — Valor adicional por criança

Cada criança adiciona R$ 50,00 ao valor da diária.

Fórmula:

`Valor da diária = valor do quarto + (quantidade de crianças × R$ 50,00)`

`Valor total = valor da diária × quantidade de noites`

Exemplo:

- 2 adultos.
- 1 criança.
- 3 noites.
- Quarto standard.

`(200 + 50) × 3 = R$ 750,00`

### RN06 — Cupons promocionais

O sistema disponibiliza dois cupons:

- HOTEL10: desconto de 10%.
- HOTEL20: desconto de 20%.

Quando nenhum cupom for informado, não haverá desconto.

Cupons desconhecidos deverão ser rejeitados.

### RN07 — Capacidade do quarto

A quantidade total de hóspedes não poderá ultrapassar a capacidade máxima da categoria escolhida.

A quantidade total será calculada pela soma de adultos e crianças.

### RN08 — Datas da reserva

- O check-in deverá ocorrer em uma data futura.
- O check-out deverá ser posterior ao check-in.
- A hospedagem deverá respeitar o limite máximo de 30 noites.

### RN09 — Disponibilidade

Um quarto não poderá possuir duas reservas ativas em períodos sobrepostos.

Reservas canceladas não deverão bloquear novos agendamentos.

### RN10 — Identificação do hóspede

Toda reserva deverá estar associada a um hóspede previamente cadastrado.

### RN11 — Cancelamento

Somente reservas existentes e ainda ativas poderão ser canceladas.

Uma reserva cancelada não poderá ser cancelada novamente.

## 5. API e rotas HTTP

A aplicação disponibilizará os seguintes endpoints:

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Página inicial |
| GET | `/health` | Verificação de funcionamento |
| GET | `/quartos` | Listar quartos |
| GET | `/hospedes` | Listar hóspedes |
| POST | `/hospedes` | Cadastrar hóspede |
| GET | `/reservas` | Listar reservas |
| POST | `/reservas` | Criar reserva |
| GET | `/reservas/{id}` | Consultar reserva |
| DELETE | `/reservas/{id}` | Cancelar reserva |

As rotas deverão retornar códigos HTTP apropriados, incluindo:

- 200 — Operação realizada com sucesso.
- 201 — Recurso criado.
- 400 — Regra de negócio violada.
- 404 — Recurso não encontrado.
- 422 — Dados de entrada inválidos.
- 500 — Erro interno inesperado.

## 6. Interface web

A aplicação deverá disponibilizar páginas HTML para interação com o sistema.

### Página inicial

Apresentação do hotel, informações gerais e acesso às funcionalidades.

### Página de quartos

Exibição das categorias, capacidades e valores das diárias.

### Página de cadastro de hóspedes

Formulário para cadastro de novos hóspedes.

### Página de reservas

Formulário para informar os dados da hospedagem, escolher o quarto, informar as datas e aplicar cupons promocionais.

### Página de consulta de reservas

Listagem das reservas existentes, com acesso aos detalhes e opção de cancelamento.

## 7. Requisitos não funcionais

### RNF01 — Desempenho

A aplicação deverá responder adequadamente a múltiplas requisições simultâneas.

O desempenho será avaliado utilizando Locust, considerando:

- Requisições por segundo (RPS).
- Tempo de resposta p95.
- Taxa de falhas.

### RNF02 — Acessibilidade

A interface deverá buscar conformidade com WCAG 2.1 nível AA.

Serão avaliados:

- Contraste de cores.
- Identificação acessível dos campos.
- Textos alternativos para imagens.
- Hierarquia dos títulos.
- Navegação por teclado.
- Visibilidade do foco.
- Identificação dos elementos interativos.

A avaliação automatizada será realizada utilizando Axe-core.

### RNF03 — Usabilidade

A interface deverá apresentar navegação clara, formulários organizados e mensagens compreensíveis de sucesso e erro.

### RNF04 — Validação

Os dados recebidos pela API deverão ser validados utilizando Pydantic.

### RNF05 — Manutenibilidade

O código deverá ser organizado em módulos, com separação entre rotas, schemas, serviços e apresentação.

### RNF06 — Confiabilidade

Falhas em serviços externos simulados não deverão comprometer os dados já registrados no sistema.

## 8. Tecnologias

- Python 3.12+
- uv
- FastAPI
- Pydantic
- Uvicorn
- Jinja2
- HTML, CSS e JavaScript
- Pytest
- pytest-mock
- Faker
- pytest-playwright
- Playwright
- axe-playwright-python
- Locust

## 9. Estratégia de testes

### Testes de integração

Utilizar TestClient para validar as rotas HTTP, códigos de resposta, payloads e regras de negócio.

Aplicar:

- Fixtures com setup e teardown utilizando yield.
- Mocks para isolamento de serviços externos.
- Faker com localização pt_BR.
- Factories para geração de dados sintéticos.
- Padrão AAA.

### Testes E2E

Utilizar Playwright para simular interações reais do usuário na interface.

Aplicar Page Object Model (POM) e seletores semânticos.

### Testes de acessibilidade

Utilizar Axe-core para auditoria automatizada e Playwright para verificar a navegação por teclado.

### Testes de carga

Utilizar Locust para simular usuários concorrentes e registrar as métricas de desempenho.

## 10. Critérios de aceitação

A aplicação será considerada adequada quando:

1. Permitir o cadastro de hóspedes.
2. Permitir a consulta de quartos.
3. Permitir a consulta de disponibilidade.
4. Permitir a criação de reservas.
5. Validar as regras de negócio da AT1.
6. Calcular corretamente os valores das hospedagens.
7. Aplicar corretamente os cupons promocionais.
8. Impedir reservas em períodos indisponíveis.
9. Permitir a consulta e o cancelamento de reservas.
10. Tratar falhas no serviço de e-mail.
11. Possuir testes de integração com Fixtures, Mocks e Faker.
12. Possuir testes E2E com Playwright e POM.
13. Possuir auditoria de acessibilidade com Axe-core.
14. Possuir testes de navegação por teclado.
15. Possuir testes de carga com Locust e métricas documentadas.

## 11. Limitações do projeto

Para manter o escopo adequado à atividade acadêmica:

- Não haverá integração com sistemas de pagamento.
- Não haverá envio real de e-mails.
- Não haverá autenticação de usuários.
- Não será utilizado banco de dados nesta versão.
- Os dados serão armazenados em memória durante a execução da aplicação.

## 12. Governança de IA

O desenvolvimento poderá contar com ferramentas de inteligência artificial como apoio à implementação, documentação e elaboração dos testes.

O uso da IA deverá ser documentado em arquivo específico, incluindo as ferramentas utilizadas, as atividades auxiliadas e os procedimentos de revisão e validação do código gerado.