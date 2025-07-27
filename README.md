# Walmart Shipping Department Database System

A comprehensive database management system for Walmart's shipping department operations, featuring data processing, storage, and analysis capabilities.

## Project Overview

This project implements a complete shipping data management solution with the following components:

- **Database Design**: SQLite-based shipping database with normalized schema
- **Data Processing**: Python scripts for CSV data ingestion and transformation
- **Data Structures**: Custom Power-of-Two Max Heap implementation in Java
- **System Architecture**: UML-designed modular processing system

## Components

### Database System (`DB_org.py`)
- Processes shipping data from multiple CSV sources
- Implements data transformation and normalization
- Manages product and shipment data insertion
- Handles data integrity and relationships

### Database Schema
The system uses a comprehensive ERD design with the following key entities:
- **Products**: Pet supplies (food, toys, apparel) with manufacturer relationships
- **Shipments**: Tracking origin/destination locations and quantities
- **Customers & Transactions**: Purchase history and customer data
- **Locations**: Warehouse and store information

### Data Structures (`PowerOfTwoMaxHeap.java`)
- Custom implementation of a power-of-two max heap
- Configurable number of children per node
- Efficient insertion and extraction operations
- Java-based implementation with proper error handling

### System Architecture (`UMLdiagram.txt`)
- Strategy pattern implementation for data processing modes
- Modular database strategy interface
- Support for multiple database backends (PostgreSQL, Redis, Elasticsearch)
- Flexible data processing pipeline

## Data Sources

The system processes shipping data from three CSV files:
- `shipping_data_0.csv`: Direct shipment records
- `shipping_data_1.csv`: Shipment identifier and product mappings
- `shipping_data_2.csv`: Origin/destination location mappings

## Usage

1. **Setup Database**: Run `python DB_org.py` to initialize the database and load data
2. **Compile Java**: `javac PowerOfTwoMaxHeap.java` to compile the heap implementation
3. **Process Data**: The system automatically handles data transformation and storage


## Requirements

- Python 3.x with pandas and sqlite3
- Java 8+ for heap implementation
- SQLite for database storage
