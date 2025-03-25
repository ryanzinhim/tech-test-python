### README: Teste 2 Avançado - Validador de IPs com API

Descrição
Implementação do Desafio 2 de forma mais profissional.
Calcula IPs válidos a partir de uma string e dessa forma há a criação de um banco de dados que guarda resultados. Uso do protocolo HTTP, Código modularizado com conexões gerenciadas e validadas.

##Estrutura
`database.py`: Configura o banco SQLite.
`data_manager.py`: Calcula IPs e gerencia dados.
`api.py`: Rotas POST `/ips/` e GET `/ips/`.

## Como Executar
`pip install -r requirements.txt`
`python database.py`
`python api.py`

## Exemplo
- POST: `curl -X POST "http://localhost:8000/ips/" -H "Content-Type: application/json" -d '{"ambiguous_ip": "1903476"}'`

  Saída: `{"resultado": ["1.90.34.76", "19.0.34.76", "190.3.4.76", "190.34.7.6"]}`
- GET: `curl "http://localhost:8000/ips/"`

(esse teste precisa ter o curl na maquina, caso não tenha, 
Basta rodar python test_api.py no terminal, com a API já ativa.)
# tech-test-python
