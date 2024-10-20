# FASTAPI Build API + Pydantic + Annotations + Pytest

Fastapi is the python webframe work used to develop the microservice apis rapidly. Its build based on starlette restapi architecture. Features of this framework are Automatic Document Generation, Validations , Security and Authentications, Dependency Injections and Supports Modern Python Types.

In this guide you will learn about how to develop basic apis ,run the application, request validations of api , annotations.

### Run the application
---

Installation and run a standard FastAPI application using `uvicorn`. It will also explain the different `uvicorn` arguments that can be used to control the behavior of your FastAPI application.

#### Step 1: Install FastAPI and Uvicorn

To get started, you need to install FastAPI and an ASGI server like `uvicorn`. You can install them using pip:

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

#### step 2: Clone the application

```bash
git clone https://github.com/python-dev-bsram/fastapi-code.git
```

#### step3: Run the app using uvicorn

To run the FastAPI application, use uvicorn with the Python file (without the .py extension) followed by the app instance. For example:

```bash
# change the directory
cd /fastapi-annotation 
```

```bash
uvicorn main:app --reload
```

- main: The name of the Python file (without .py).
- app: The FastAPI application instance.
- --reload: Automatically reload the server when code changes (useful for development).

## Uvicorn Arguments and Options

`--host`

By default, it runs on 127.0.0.1 (localhost). Use 0.0.0.0 to make it accessible from any IP address.

```bash
uvicorn main:app --host 0.0.0.0
```

``--port``

Defines the port on which the server will run.

```bash
uvicorn main:app --port 8001
```

``--reload``

Enables auto-reloading of the server when the code is modified. This is especially useful in development mode.

```bash
uvicorn main:app --reload
```

``--workers``

Defines the number of worker processes to run. This is useful in production environments where you need more performance.

```bash
uvicorn main:app --workers 4
```

``--log-level``

Sets the logging level. Options include critical, error, warning, info, debug, and trace.

```bash
uvicorn main:app --log-level debug
```

``--limit-concurrency``

Limits the maximum number of concurrent connections that Uvicorn will accept

```bash
uvicorn main:app --limit-concurrency 100
```

``--timeout-keep-alive``

Defines the timeout (in seconds) for keeping a connection alive

```bash
uvicorn main:app --timeout-keep-alive 60
```
`--proxy-headers`

Enables the handling of X-Forwarded-Proto and X-Forwarded-For headers, useful when running the app behind a proxy.
```bash
uvicorn main:app --proxy-headers
```

`--env-file`

Specifies a .env file to load environment variables from.

```bash
uvicorn main:app --env-file .env
```

`--app-dir`

Specifies a directory where the application module is located. This is useful if the app is not in the current working directory.

```bash
uvicorn app_name:app --app-dir /path/to/your/app
```

`--ssl-keyfile` and `--ssl-certfile`

Enable SSL (HTTPS) by specifying the key and certificate files.

```bash
uvicorn main:app --ssl-keyfile ./key.pem --ssl-certfile ./cert.pem
```




