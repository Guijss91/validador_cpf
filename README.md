# API de Validação de CPF

- GET / -> "A API está rodando"
- POST /verificar -> body JSON: {"cpf": "123.456.789-09"} retorna {"valido": true|false, "cpf": "12345678909"}


POST:
curl -s -X POST http://localhost:8000/verificar \
  -H "Content-Type: application/json" \
  -d '{"cpf":"12345678909"}'

## Docker

Build:
docker build -t cpf-api:latest .

Run:
docker run --rm -p 8000:8000 cpf-api:latest
