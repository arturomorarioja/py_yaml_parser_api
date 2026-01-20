# YAML Parsing
API that returns a parsed sample YAML file with information about fake Danish companies.

## Usage
1. Start the Docker container: `docker compose up -d`
2. In a user agent (browser, Postman, etc.), access `http://localhost:8080/parse/` plus the route of the YAML file, relative to the container root (e.g., for the test YAML file in `/test_data`, access `http://localhost:8080/parse/test_data/danish_companies.yml`).
3. Finalise the application by stopping the container: `docker compose down`

## Tools
Flask / Python

## Author
ChatGPT 5.1, prompted by Arturo Mora-Rioja