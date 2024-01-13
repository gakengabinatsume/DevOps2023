# How to add Prometheus and Grafana to Jenkins

**Step 1 : Add the Prometheus pluggin in Jenkins and configure it.**

![Prometheus_config](https://github.com/gakengabinatsume/DevOps2023/assets/141765846/ad2b35e7-eb6c-4c3f-8e8e-04f76863c9c3)

**Step 2 : Create the stack using Docker in the monitoring folder**

Files nedded:
- docker-compose.yaml
- prometheus.yaml

`mkdir monitoring`

`mv docker-compose.yaml monitoring`

`mkdir prometheus`

`mv prometheus.yaml prometheus`

`sudo docker-compose up -d`

![docker compose up](https://github.com/gakengabinatsume/DevOps2023/assets/141765846/ddb127e7-2b8e-4f6a-8283-070c004cfc21)

**Step 3 : Configure Prometheus and Grafana on the localhost**



**Step 4 : Pull the image from Dockerhub and run it**
