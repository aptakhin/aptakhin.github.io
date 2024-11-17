---
marp: true
footer: 'Alexander Ptakhin for PyBerlin 2024 Nov 27th'
---

<!-- theme: uncover -->
<!-- headingDivider: 2 -->

<!-- FastAPI is awesome! I’ll share my experience designing larger applications, improving the structure of monoliths, and handling API/database migrations. We’ll discuss usage Depends vs. DI containers, straightforward ways to implement tests (unit to e2e), and how to configure logging/tracing for better observability. Plus, I’ll touch on deployment strategies.

I aim for this talk to offer developers and leads, even those using different frameworks, practical insights on ensuring better testability and observability in services.

-->

# Hello

# Hello

The standard slide why I'm expert.
Around 10 years with Python.
C++, Python 2, Python 3, JavaScript.

Monolyths, distributed systems.

<!-- note: Not very heavy-loaded, otherwise. why Python -->

<!-- paginate: true -->

# Enterprise?

<!-- Sounds awkward. A little bit boring Java and C# -->

# Enterprise?
It’s word for boring.

<!-- note: In the startup it will not boring, you deprecate and break one things, but the new are still not ready -->


# he?

- Problems
- Architecture
- Design
- Deployment



<!-- - We generally don't drop data, but mark DELETED -->
<!-- - Even in GDPR we left it's DELETED -->


<!-- >
We thought about how to deploy before we started coding.
How we should organize.
Which stack shold we go.
Code organization.
Folder. Modules.
Count coupling
-->


# Context

Up to four developers.

1,5 years of development. We don’t have reasons to have two repositories for the frontend and backend.

Microservices. About definitions between authors.
Independently deployable units. If we have temporal deployment coupling, we possibly have a problem.
2 deployments + ingress.


Services approach. Zitadel.

Developers experience.


# CI/CD

# Tests

Acceptance.
Integration.
Unit.

<!-- schema -->

# API Versioning

Versioning of API endpoint.
Routers.


# Acceptance example

cypress call.

# Integration

API calls included. Database included. Sending emails not.


# Unit tests
No dependencies.
Very fast.
Fast tests < 10 seconds for Ctrl+S.
pytest-watcher.

# ptw --now .

# pre-commit

ruff format, ruff check.

# Pipelines pain
- Everything in bash for pipelines.
- Run bash or python.
- Testeable locally
- Click as less buttons as you can
- Write as less yaml as you can


Weekly releases.

# Bash


Pre-commit. Fast tests < 10 seconds, ruff format, ruff check.
Pipelines: everything longer.
Costly acceptance cypress tests.

# Database migrations

Database migrations. Big topic.

We make small changes. We have a few data. We can do anything.
But on scale it's not true.

Migrate parts by parts.

# Our enterprease stops here.

Better developers learn SQL than ORM.
But straightforward SQLBuilder is good enough not to start dealing with generation strings %1, %2.

# Auth0

Auth0. Implement it yourself.

# Depends

Depends, DI. Container.

```python
async def init() -> None:
    database = Database(settings.database_dsn)
    container.register(Database, instance=database)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init()
    yield


app = FastAPI(lifespan=lifespan)
```

#  Metrics

```python

```


# Middleware

- /metrics
- Decorators

decorators. Endpoints.
Simple approach. Auth states.
Router variables?
Inside login. User.

# Tests

Unit tests
Integration tests
e2e acceptance

Test prod with cypress. Monitor errors.

# Happily tested
Is that's all?

# Logs

Logs:
JSON
Pretty print in console.

# Metrics

Prometheus.

# Traces

Helpers install: will make 50% percents
The rest on us

# Grafana


# Docker

Docker compose.

Caching images.
Pipenv, poetry, uv

# Other

# Contacts

X, Mastodont, Bluesky
