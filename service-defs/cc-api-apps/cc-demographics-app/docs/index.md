# NHS Access Token API

This API retrieves and provides NHS access token for NHS Rest calls. Additionally provides service health monitoring, basic system information retrieval.
This application has following endpoints:
- `/api/nhs-access-token/v1/info`
- `/api/nhs-access-token/v1/healthz`
- `/api/nhs-access-token/v1/token`

## Base URLs
APIM URL's
---

## 1. Health Check
Verifies the operational status of the service and its downstream dependencies.
(Future enhancement, check for NHS interface accessibility)
### Endpoint
`GET /api/nhs-access-token/v1/healthz`

### Response
Returns a `200 OK` if the service is healthy.

```json
{
  "status": "up",
  "timestamp": "2026-06-03T15:58:00Z"
}
```

---
## 2. Get System Info
Retrieves basic metadata about the running application instance.

### Endpoint
`GET /api/nhs-access-token/v1/info`

### Response
Returns a `200 OK` with build and environment details.

```json
{
  "app_name": "nhs-access-token-api-info",
  "version": "1.0.0",
  "environment": "production",
  "hostname": "",
  "timestamp": current timestamp,

}
```

---
## 3. Get NHS Access Token
Generates a short-lived NHS OAuth2 access token using client credentials.

### Endpoint
`GET /api/nhs-access-token/v1/token`

### Request Headers

| Header | Type | Description |
| :--- | :--- | :--- |
| `x-api-key` | API Key | **Required.** |

### Response
Returns a `200 OK` with the nhs token response containing access token

```json
{
  "access_token": "oSqpmZas6wbg4w49rGYaeUA4ijB1",
  "expires_in": "599",
  "issued_at": "1780497533286",
  "token_type": "Bearer"
}
```

### Error Responses

| Status Code | Reason | Sample Payload |
| :--- | :--- | :--- |
| `500 Internal server error` | NHS request error | `{"error": "nhs request error details"}` 
