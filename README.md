# ELK Stack Setup

This repository contains a Docker Compose configuration for setting up the ELK (Elasticsearch, Logstash, Kibana) stack.

## Prerequisites

- Docker
- Docker Compose

## Installation

1. Make sure Docker and Docker Compose are installed on your system
2. Clone this repository or download the files
3. Open a terminal in the project directory
4. Run the following command to start the ELK stack:
   ```bash
   docker-compose up -d
   ```

## Accessing the Services

- Elasticsearch: http://localhost:9200
- Kibana: http://localhost:5601
- Logstash: 
  - TCP: localhost:5000
  - UDP: localhost:5000
  - Beats: localhost:5044

## Configuration

- The Logstash pipeline configuration is located in `logstash/pipeline/logstash.conf`
- Elasticsearch data is persisted in a Docker volume named `elasticsearch-data`

## Stopping the Stack

To stop the ELK stack, run:
```bash
docker-compose down
```

## Notes

- This setup uses the latest stable version of ELK (8.12.1)
- Security features are disabled for development purposes
- Memory limits are set to reasonable defaults for development
- For production use, please adjust the configuration accordingly 