# pynest-grafana-example
Pynest + Postgres + Grafana + Docker example

### Quick Start
1. Install Loki driver

`docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions`

2. Enable Loki plugin

`docker plugin enable loki`

3. Start Docker Compose services

`docker-compose up -d`


## Reference
[fastapi-observability](https://github.com/blueswen/fastapi-observability)

[PyNest](https://github.com/PythonNest/PyNest)
