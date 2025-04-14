# 💱 API de Cotação de Moedas (FastAPI + Redis + MySQL + Docker)

Projeto de microserviços com FastAPI para consultar a cotação de moedas. O sistema utiliza múltiplas fontes de dados com fallback e caching inteligente:

- 🔁 Redis para cache
- 🛢️ MySQL para persistência
- 🌐 [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) como fonte externa

---

## 🧩 Arquitetura

Este projeto está dividido em dois microserviços:

- **api_Consome (porta 8000):** Interface pública que faz requisições para `api_Moeda`.
- **api_Moeda (porta 8001):** Responsável pela lógica de cache, banco de dados e fallback à API externa.

> Ambos são executados como containers independentes com Docker Compose.

---

## 📦 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Redis](https://redis.io/)
- [MySQL 8](https://www.mysql.com/)
- [Docker & Docker Compose](https://docs.docker.com/compose/)
- [Requests](https://pypi.org/project/requests/)

---

## ⚙️ Como Funciona

1. **O usuário acessa `/cotacao/{moeda}`** via `api_Consome`.
2. Essa rota chama a `api_Moeda`, que faz:
   - Busca no **Redis** (cache);
   - Se não encontrar, tenta o **MySQL**;
   - Se ainda assim não encontrar, chama a **AwesomeAPI**;
   - O valor obtido é cacheado no Redis por **1 hora**.

---

## 🚀 Como Executar

### Pré-requisitos

- Docker e Docker Compose instalados

### Passos para rodar o projeto:

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/api-cotacao-moedas.git
cd api-cotacao-moedas


