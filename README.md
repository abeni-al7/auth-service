# Auth Service

## Environment Variables

The application's configuration is managed using environment variables, which can be provided through a `.env.{ENVIRONMENT}` file or set directly in the environment.

### Configuration Loading

The configuration is loaded with the following precedence:

1.  **Environment Variables**: Any configuration variable set directly in the shell environment will take the highest precedence.
2.  **.env file**: If not set in the shell, the application will try to load variables from a `.env` file. The specific file loaded depends on the `ENVIRONMENT` variable (e.g., `.env.dev`, `.env.prod`, `env.test`). If `ENVIRONMENT` is not set, it defaults to loading from `.env.dev`.

### Variables

| Variable             | Description                                                                                              | Default Value |
| -------------------- | -------------------------------------------------------------------------------------------------------- | ------------- |
| `APP_NAME`           | The name of the application.                                                                             | "Auth service"  |
| `PORT`               | The port on which the application server will listen.                                                    | `8000`          |
| `DEBUG`              | Toggles debug mode for the application. Set to `True` for development to get more verbose error messages.  | `False`         |
| `DATABASE_URI`       | The connection string for the PostgreSQL database.                                                       | -             |
| `JWT_SECRET`         | A strong, secret key used for signing JWTs. It must be at least 32 characters long.                        | -             |
| `JWT_EXPIRY_SECONDS` | The duration in seconds for which a JWT will be valid.                                                   | `3000`          |
| `ENVIRONMENT`        | Determines which `.env` file to load (e.g., `dev` loads `.env.dev`).                                       | `dev`           |

## Database Migrations

This project uses Alembic to manage database schema migrations. Before running migration commands, ensure your `DATABASE_URI` is correctly configured in your `.env` file and that the database server is accessible.

### Creating a New Migration

After modifying the SQLAlchemy models (e.g., in `src/models/user.py`), you can automatically generate a migration script that reflects your changes.

```bash
alembic revision --autogenerate -m "A short description of the model changes"
```

This command compares the models against the current database schema and generates a new revision file in `alembic/versions/`.

### Applying Migrations

To apply all pending migrations and bring the database schema up to date with the latest revision, run:

```bash
alembic upgrade head
```

### Downgrading Migrations

To revert the last applied migration, use:

```bash
alembic downgrade -1
```

To revert all migrations and return the schema to its initial state, use:

```bash
alembic downgrade base
```

## Running Tests

To run the automated tests for this service, you can use Python's built-in `unittest` module.

From the root directory of the project, run the following command:

```bash
python -m unittest discover tests
```

This command will automatically discover and run all tests within the `tests` directory.
