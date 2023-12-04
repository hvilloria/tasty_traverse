# Welcome to Tasty Traverse

## Quick Start

If you are a new, this is the quickest way to get the app running.

- Get Docker Desktop installed
- Copy the `example_env` file to a new file named `.env`
- Open a terminal in the repository directory and run:
    * `docker compose exec -it tasty_web bash`
    * `flask db upgrade` to run migrations
- to bring up the stack:
    * `docker compose up`
