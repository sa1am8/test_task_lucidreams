# Project Name

This is a FastAPI project that uses Poetry for dependency management and MySQL for the database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/username/project.git
    ```

2. Install the dependencies using Poetry:
    ```bash
    poetry install
    ```

3. Create a `.env` file in the root directory and add your database credentials:
    ```env
    DATABASE_URI=mysql+pymysql://username:password@localhost:3306/dbname
    ```

4. Run the FastAPI server:
    ```bash
    poetry run uvicorn main:app --reload
    ```