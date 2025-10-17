# Polyglot NLP Toolkit 🚀
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hacktoberfest](https://img.shields.io/badge/Hacktoberfest-2025-blue.svg)](https://hacktoberfest.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Issues](https://img.shields.io/github/issues/ayaantuts/nlp-polyglot)](https://github.com/ayaantuts/nlp-polyglot/issues)
[![Good First Issues](https://img.shields.io/github/issues/ayaantuts/nlp-polyglot/good%20first%20issue?label=Good%20First%20Issues)](https://github.com/ayaantuts/nlp-polyglot/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

A web-based toolkit for performing powerful NLP analysis on text in multiple languages. This project provides a simple interface to complex models for tasks like Sentiment Analysis, Named Entity Recognition, and more.

### [Live Demo Link (Coming Soon!)](https://nlp-polyglot.vercel.app/)

---

## Features

- **Multilingual Support:** Analyze text in various languages thanks to state-of-the-art multilingual models.
- **Sentiment Analysis:** Determine if a block of text is positive, negative, or neutral.
- **Named Entity Recognition (NER):** Identify and extract entities like people, places, and organizations.
- **Text Summarization:** Condense long articles into a few key sentences.
- **Clean, Modern UI:** A simple and intuitive interface built with React.js.

## Tech Stack

| Area      | Technology                                                                                                                              |
| :-------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend** | ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) |
| **Backend** | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)     |
| **Database** | ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)                                |
| **NLP Models**| ![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Transformers-FFD21E.svg)                                     |
| **DevOps** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)                                    |

---

## Screenshots

Coming Soon!

---

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Git
- Node.js & npm
- Python 3.13+ & pip
- MongoDB (running locally or via a free cloud instance like MongoDB Atlas)
<!-- - Docker (optional, but recommended for easy setup) -->

### 1. Local Installation

**A. Fork and Clone the Repository**

```bash
git clone https://github.com/ayaantuts/nlp-polyglot.git
cd nlp-polyglot
```

**B. Backend Setup**

```bash
cd backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your MongoDB connection string
echo "MONGO_URI=your_mongodb_connection_string" > .env

# Run the Flask server
flask run
```
The backend will be running at `http://127.0.0.1:5000`.

**C. Frontend Setup**

```bash
# Open a new terminal
cd frontend

# Install dependencies
npm install

# Create a .env.local file to point to the backend API
echo "NEXT_PUBLIC_API_URL=http://127.0.0.1:5000" > .env.local

# Run the Next.js development server
npm run dev
```
The frontend will be running at `http://localhost:3000`.

<!-- ### 2. Docker Setup (Easy Mode)

If you have Docker installed, you can get everything running with one command.

```bash
# Make sure to create the .env and .env.local files as described above!
docker-compose up --build
``` -->

---

## How to Contribute

We welcome contributions of all kinds! This is a perfect project for **Hacktoberfest**.

Please read our **[CONTRIBUTING.md](CONTRIBUTING.md)** to learn how you can get involved, from reporting bugs to submitting pull requests.

## License

This project is licensed under the MIT License. See the **[LICENSE](LICENSE)** file for details.