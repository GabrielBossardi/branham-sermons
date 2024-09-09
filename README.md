# Branham Sermons

This project is designed to parse and store William Branham's sermons in a PostgreSQL database.

## Project Structure

The project consists of the following main components:

1. A Python script (`parse.py`) to parse sermon data from a JSON file and store it in a PostgreSQL database.
2. A Docker Compose configuration for setting up the PostgreSQL database.
3. Poetry for managing Python dependencies.

## Prerequisites

- Python 3.11 or higher
- Docker and Docker Compose
- Poetry

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd branham-sermons
```

2. Install dependencies using Poetry:
```bash
poetry install
```


3. Create a `.env` file in the project root with the following content:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```


4. Start the PostgreSQL database using Docker Compose:
```bash
docker-compose up -d
```


## Usage

1. Ensure you have a `sermons.json` file in the `data/` directory containing the sermon data.

2. Run the parsing script:
```bash
poetry run python parse.py
```

This will parse the JSON data and store it in the PostgreSQL database.

## Database Schema

The `sermons` table in the database contains the following columns:

- id
- title
- date
- date_display_name
- date_day_period (if available)
- location_country (if available)
- location_country_abbv (if available)
- location_state (if available)
- location_state_abbv (if available)
- location_city
- building
- audio

## Project Configuration

The project uses Poetry for dependency management. The `pyproject.toml` file contains the project configuration and dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
