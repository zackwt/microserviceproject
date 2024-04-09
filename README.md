# microserviceproject
## Requirements
Write a microservices application that runs in docker compose. Services must be in separate containers and may not have shared code. Services must include:

## Acceptence Criteria
1. Node Server front end written in react
2. Python API backend in Django
3. Database with MySQL
4. Authentication service using stateless JWT

# Stack:
    * React
    * Django
    * MySQL

# Description
Utilizing the previously described stack and requirements I will be building a Full Stack microservices application. This application will be an e commerce application designed for the Yu-Gi-Oh! trading card game. Users will be able to create an account and login, browse available products, add products to their cart, and checkout products. 

# Data Model
| User           |Product    |Category   |Order     |OrderItem|Cart|CartItem|Payment|Shipping|Review|
|----------------|-----------|-----------|----------|---------|----|--------|-------|--------|------|
|ID (PK)         |ID (PK)    |ID (PK)    |ID (PK)   |
|Username        |Name       |Name       |Order Date|
|Password        |Description|Parent     |User (FK) |
|Email           |Price      |Description|Total     |
|Full Name       |Stock      |Image      |Status    |
|Shipping Address|Category   |
|Billing Address |Image      |
|Phone Number    |
