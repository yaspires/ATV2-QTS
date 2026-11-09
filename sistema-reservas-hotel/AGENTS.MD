# AGENTS.md — Regras de Contexto do Projeto

## 1. Contexto do projeto

Este projeto consiste em um Sistema Web de Reservas de Hotel, desenvolvido como atividade acadêmica da disciplina Qualidade e Teste de Software (QTS).

O objetivo é implementar uma aplicação web utilizando Python, FastAPI, Pydantic e HTML, acompanhada de testes de integração, testes End-to-End, auditoria de acessibilidade e testes de carga.

O documento `PRD.md` é a principal referência para os requisitos e regras de negócio.

## 2. Tecnologias obrigatórias

- Python 3.12 ou superior.
- uv para gerenciamento do projeto e dependências.
- FastAPI para construção da API.
- Pydantic para validação de dados.
- Jinja2 para renderização de páginas HTML.
- Pytest para execução dos testes.
- pytest-mock para criação de mocks.
- Faker com localização pt_BR para dados sintéticos.
- Playwright para testes E2E.
- axe-playwright-python para auditoria de acessibilidade.
- Locust para testes de carga.

Não introduzir tecnologias adicionais sem necessidade ou justificativa.

## 3. Organização do código

Manter a separação de responsabilidades:

- `app/routes/`: definição das rotas HTTP.
- `app/schemas/`: modelos e validações Pydantic.
- `app/services/`: regras de negócio e operações do sistema.
- `app/templates/`: páginas HTML.
- `app/static/`: arquivos CSS e JavaScript.
- `tests/integration/`: testes de integração.
- `tests/e2e/`: testes End-to-End.
- `tests/e2e/pages/`: classes Page Object Model.
- `tests/accessibility/`: testes de acessibilidade.
- `tests/factories/`: geração de dados sintéticos.

Evitar duplicação de código e manter nomes claros e descritivos.

## 4. Regras de implementação

- Utilizar Type Hints nas funções e métodos.
- Adotar nomes de variáveis e funções em português, mantendo nomes técnicos das bibliotecas quando necessário.
- Separar regras de negócio da camada de apresentação.
- Utilizar tratamento defensivo de exceções.
- Não utilizar valores fixos desnecessários espalhados pelo código.
- Não utilizar dados reais de pessoas nos testes.
- Garantir respostas HTTP coerentes com os resultados das operações.
- Manter as validações consistentes entre a API e as regras de negócio.

## 5. Regras de negócio

As regras descritas no `PRD.md` devem ser respeitadas integralmente.

As regras de cálculo herdadas da AT1 não devem ser modificadas sem justificativa e aprovação.

Os valores dos quartos são:

- Standard: R$ 200,00 por noite.
- Luxo: R$ 350,00 por noite.
- Suíte: R$ 500,00 por noite.

Cada criança adiciona R$ 50,00 à diária.

Cupons disponíveis:

- HOTEL10: 10% de desconto.
- HOTEL20: 20% de desconto.

A quantidade de adultos, crianças e noites deve respeitar os limites definidos no PRD.

## 6. Padrões de testes

Todos os testes devem utilizar o padrão AAA:

- Arrange: preparação dos dados e condições.
- Act: execução da operação testada.
- Assert: verificação dos resultados.

Utilizar:

- `@pytest.mark.integration` para testes de integração.
- `@pytest.mark.e2e` para testes End-to-End.
- `@pytest.mark.accessibility` para testes de acessibilidade.
- `@pytest.fixture` para preparação de recursos.
- `yield` nas fixtures que necessitam de teardown.
- `@pytest.mark.parametrize` quando houver diferentes cenários para uma mesma funcionalidade.

Os testes de integração devem utilizar TestClient.

As dependências externas devem ser isoladas por meio de mocks.

Os dados sintéticos devem ser gerados utilizando Faker("pt_BR") e Factories.

Os testes E2E devem utilizar Playwright e Page Object Model.

Os seletores devem priorizar elementos semânticos, como `get_by_role`, `get_by_label` e `get_by_text`.

Os testes de acessibilidade devem utilizar Axe-core e verificar a navegação por teclado.

## 7. Governança de Inteligência Artificial

A inteligência artificial poderá ser utilizada como ferramenta de apoio para:

- Planejamento e organização do projeto.
- Sugestões de implementação.
- Explicação de conceitos e tecnologias.
- Elaboração e revisão de testes.
- Identificação de possíveis erros.
- Apoio à documentação.

Todo código sugerido por IA deverá ser revisado e compreendido antes de sua utilização.

Não aceitar implementações automaticamente sem verificar se atendem ao PRD.

Não inventar resultados de testes, métricas de desempenho ou evidências de execução.

As informações sobre o uso da IA deverão ser documentadas no arquivo `AI_USAGE.md`.

## 8. Documentação e manutenção

- Manter o `README.md` atualizado com instruções de instalação e execução.
- Utilizar `uv` para instalar e executar as dependências.
- Atualizar o `uv.lock` quando houver alterações nas dependências.
- Documentar alterações importantes.
- Manter o PRD atualizado caso os requisitos sejam modificados.

## 9. Diretrizes gerais

Priorizar simplicidade, legibilidade, organização e confiabilidade.

Não implementar funcionalidades que estejam fora do escopo definido sem necessidade.

Toda implementação deverá possuir justificativa e estar alinhada aos requisitos da atividade AT2.