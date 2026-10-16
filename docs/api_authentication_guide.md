# Internal API Authentication Guide

**Document ID:** ENG-DOC-101
**Owner:** Platform Engineering
**Applies to:** Services calling internal REST APIs

## 1. Overview
All internal APIs behind the `api.internal.company.example` gateway require
authentication using short-lived OAuth 2.0 client-credentials tokens issued
by the internal Auth Service.

## 2. Obtaining a Token
```
POST https://auth.internal.company.example/oauth2/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
client_id=<your-service-client-id>
client_secret=<your-service-client-secret>
scope=api.read api.write
```
The response includes an `access_token` valid for 3600 seconds and a
`token_type` of `Bearer`.

## 3. Calling an API
Include the token in the `Authorization` header:
```
GET /v1/employees HTTP/1.1
Host: api.internal.company.example
Authorization: Bearer <access_token>
```

## 4. Scopes
| Scope | Grants |
|-------|--------|
| api.read | Read-only access to non-sensitive resources |
| api.write | Create/update access |
| api.admin | Administrative operations, requires security review to obtain |

## 5. Rotating Credentials
Client secrets expire every 90 days automatically. A rotation reminder is
sent to the service owner 14 days before expiry via the Auth Service
dashboard. Secrets can be rotated early via `POST /oauth2/clients/{id}/rotate`.

## 6. Rate Limits
Default rate limit is 100 requests/second per client_id. Requests exceeding
this return `429 Too Many Requests` with a `Retry-After` header. Teams
needing higher limits should file a request with Platform Engineering.

## 7. Local Development
For local development, use the sandbox auth server at
`auth.sandbox.company.example`, which issues non-expiring test tokens tied
to fake client IDs listed in the `platform-eng/dev-credentials` internal
repo.
