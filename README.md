# EcoGrid Energy - Python Fitness Functions

This is a lightweight prototype used to demonstrate automated architectural fitness functions for the ICT 711 EcoGrid Energy design.

## Included checks
- Smart-meter ingestion throughput
- Marketplace response latency
- Financial settlement idempotency
- Bounded-context dependency rule
- Event schema compatibility

## Run locally

```bash
pip install -r requirements.txt
pytest fitness_functions -q
```

## CI/CD

The GitHub Actions workflow in `.github/workflows/fitness-functions.yml` runs the fitness functions automatically on every push and pull request.

## Note

The thresholds are prototype fitness thresholds for assessment demonstration. They are not production benchmarks.
