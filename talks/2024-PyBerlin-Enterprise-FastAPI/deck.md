---
marp: true
footer: 'Alexander Ptakhin for PyBerlin 2024 Nov 27'
---

<!-- theme: uncover -->
<!-- headingDivider: 2 -->

<!-- FastAPI is awesome! I’ll share my experience designing larger applications, improving the structure of monoliths, and handling API/database migrations. We’ll discuss usage Depends vs. DI containers, straightforward ways to implement tests (unit to e2e), and how to configure logging/tracing for better observability. Plus, I’ll touch on deployment strategies.

I aim for this talk to offer developers and leads, even those using different frameworks, practical insights on ensuring better testability and observability in services.

-->

# Hello

# Hello

The standard slide why I'm expert.

# Enterprise?

# Enterprise?
It’s word for boring.
<!-- paginate: true -->

# he?

We thought about how to deploy before we started coding.
How we should organize.
Which stack shold we go.
Code organization.
Folder. Modules.
Count coupling


# Context

Up to four developers.

1,5 years of development. We don’t have reasons to have two repositories for the frontend and backend.

Microservices. About definitions between authors.
Independently deployable units. If we have temporal deployment coupling, we possibly have a problem.
2 deployments + ingress.


Services approach. Zitadel.

Developers experience.


# CI/CD


# Bash
Everything in Bash for pipelines.
Run bash

Pre-commit. Fast tests < 10 seconds, ruff format, ruff check.
Pipelines: everything longer.
Costly acceptance cypress tests.

# API Versioning

Everything
Versioning of APIs.
Routers.

# Database migrations

Database migrations. Big topic.

Better developers learn SQL than ORM.
But straightforward SQLBuilder is good enough not to start dealing with generation strings %1, %2.

# Auth0

Auth0. Implement it yourself.

# Depends

Depends, DI.
States FastAPI.


Metrics.
Middleware.
Decorators.
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
Pretty print in console

# Metrics

Prometheus.

# Traces

# Grafana

# Docker

Docker compose.

Caching images.
Pipenv, poetry.

# Other
