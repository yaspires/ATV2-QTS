# Sistema Web de Reservas de Hotel

Projeto desenvolvido para a disciplina de Qualidade e Teste de Software (QTS) — Fatec.

A aplicação permite o cadastro de hóspedes, consulta de quartos e gerenciamento de reservas de hospedagem por meio de uma interface web.

---

## Tecnologias utilizadas

- Python 3.12+
- uv (gerenciamento de ambiente e dependências)
- FastAPI
- Pydantic
- Uvicorn
- Jinja2
- Pytest
- pytest-mock
- Faker
- Playwright
- axe-playwright-python
- Locust

---

## Instalação

### Pré-requisitos

- Python 3.12 ou superior instalado
- uv instalado ([instruções](https://docs.astral.sh/uv/getting-started/installation/))

### Passos

Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/yaspires/ATV2-QTS.git
cd sistema-reservas-hotel
```

Instale as dependências:

```bash
uv sync
```

Instale o navegador do Playwright:

```bash
uv run playwright install chromium
```

---

## Execução da aplicação

```bash
uv run uvicorn app.main:app --reload
```

Acesse no navegador: [http://localhost:8000](http://localhost:8000)

---

## Rotas disponíveis

| Método | Rota | Descrição |
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
| GET | `/pagina-hospedes` | Interface de hóspedes |
| GET | `/pagina-reservas` | Interface de reservas |

---

## Execução dos testes

### Todos os testes

```bash
uv run pytest -v
```

### Testes de integração

```bash
uv run pytest tests/integration/ -v
```

### Testes E2E

```bash
uv run pytest tests/e2e/ -v
```

### Testes de acessibilidade

```bash
uv run pytest tests/accessibility/ -v
```

### Por marcação

```bash
uv run pytest -m integration -v
uv run pytest -m e2e -v
uv run pytest -m accessibility -v
```

---

## Testes de carga com Locust

Inicie a aplicação em um terminal:

```bash
uv run uvicorn app.main:app
```

Em outro terminal, execute o Locust:

```bash
uv run locust -f locustfile.py --host http://localhost:8000
```

Acesse a interface do Locust em [http://localhost:8089](http://localhost:8089), configure o número de usuários e inicie a simulação.

### Métricas registradas

Execução realizada com 10 usuários simultâneos:

| Métrica | Resultado |
|---|---:|
| Usuários simultâneos | 10 |
| Total de requisições | 53 |
| Requisições por segundo (RPS) | 3,9 |
| Tempo médio de resposta | 6,69 ms |
| Mediana | 3 ms |
| Percentil 95 (p95) | 22 ms |
| Percentil 99 (p99) | 73 ms |
| Tempo máximo | 73 ms |
| Taxa de falhas | 0% |

> Os resultados foram obtidos em ambiente local e podem variar conforme a máquina e a carga do sistema operacional.

---

## Limitações conhecidas

- Os dados são armazenados em memória e são perdidos quando a aplicação é reiniciada.
- Não há autenticação de usuários.
- Não há integração com sistemas de pagamento.
- O envio de e-mails é simulado e não realiza envios reais.
- Não há banco de dados persistente.

---

## Estrutura do projeto

```text
sistema-reservas-hotel/
├── app/
│   ├── main.py
│   ├── data/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── templates/
│   └── static/
├── tests/
│   ├── conftest.py
│   ├── integration/
│   ├── e2e/
│   │   └── pages/
│   ├── accessibility/
│   └── factories/
├── PRD.md
├── AGENTS.md
├── AI_USAGE.md
├── locustfile.py
├── pyproject.toml
└── uv.lock
```

---

## Documentação adicional

- [`PRD.md`](PRD.md) — Requisitos e especificações do sistema
- [`AGENTS.md`](AGENTS.md) — Regras de contexto do projeto
- [`AI_USAGE.md`](AI_USAGE.md) — Relatório de uso de inteligência artificial
