# StockFlow

**StockFlow is a lightweight Point-of-Sale (POS) system built for small and growing businesses.**

It is designed to help businesses manage day-to-day sales, products, customers, and inventory through a simple operational system.

StockFlow is being developed with small and medium-sized businesses in mind, with a focus on practical operations, simplicity, and accessibility.

## Current Features

- Product management
- Inventory tracking
- Sales processing
- Customer management
- Sales history
- Automatic stock updates after sales
- Product and customer search
- Unique sale IDs
- Structured data models
- Database-backed data storage

## Tech Stack

- **Python** — core application logic
- **SQLite** — database
- **Pydantic** — data schemas and models
- **Pytest** — automated testing

## Project Structure

```text
StockFlow/
│
├── data/
│   ├── stockflow.db
│   ├── products.json
│   ├── sales.json
│   └── customers.json
│
├── tests/
│
├── models/
│
├── main.py
└── README.md
```

> The project structure is actively evolving as StockFlow moves from JSON-based storage toward a structured database architecture.

## Development

StockFlow is currently under active development.

The project is transitioning from its original JSON-based data storage approach to a SQLite database with structured Pydantic models.

Automated testing is being introduced alongside the new architecture to ensure the core functionality remains reliable as the system evolves.

## Current Development Direction

The current development focus is:

1. Establish structured data schemas
2. Transition data storage from JSON to SQLite
3. Add data validation
4. Expand automated testing
5. Strengthen the core POS functionality

The existing JSON files are currently retained during the transition and may be removed once the database implementation is fully established.

## Planned Features

- Improved POS interface
- Offline-first operation
- Receipt generation
- Business reporting and analytics
- WhatsApp-based POS interaction
- API integration
- Additional business and payment integrations

## Vision

StockFlow aims to make modern business operations more accessible to small and medium-sized businesses.

A business should be able to manage its sales and inventory whether it operates from a physical storefront, sells online, or primarily takes orders through platforms such as WhatsApp.

The long-term goal is to provide a flexible POS system that can adapt to how different small businesses actually operate.

**Built by Flexure.**
