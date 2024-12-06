# Capital Gains

This repository contains a Python script that calculates taxes for a list of operations provided via the command line or an input file (`input.txt`). The application runs inside a Docker container and includes unit tests to ensure code reliability.

---

## Requirements

Before starting, make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Python 3.11](https://www.python.org/downloads/) (optional, for local development)

---

## How to run

### Build the container

```bash
docker build -t test-nubank .
```

### Run the Container

Run the container using input.txt

```bash
docker run -i test-nubank < input.txt
```

Run the container passing parameters on command line

```bash
docker run -i test-nubank <<EOF
<line1>
<line2>
EOF
```

### Run without Docker

Run passing parameters on input.txt

```bash
python3 main.py < input.txt
```

Run passing parameters on command line

```bash
python3 main.py
```

Type de lines and press **ctrl+D** to run script.