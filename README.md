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
