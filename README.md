# FK-Kulukorvauslomake
A website that collects reimbursement requests

- [Getting started](#getting-started)
  * [Admin interface](#admin-interface)
- [System instructions](#system-instructions)
  * [Production mode](#production-mode)
  * [Development mode](#development-mode)

## Getting started
Users can submit general and travel reimbursements.

### Admin interface

## System instructions
These instructions will walk you through the steps to start hosting this service in your environment.

### Production mode

### Development mode
Start the service in development mode using
```commandline
docker-compose -f docker-compose.yml --env-file .env up -d
```

Stop the service with
```commandline
docker-compose -f docker-compose.yml down
```