 # REST API Architecture and FastAPI


### Key Features of REST API:
1. **Stateless**: Each request from a client to a server must contain all the information needed to understand and process the request.
2. **Client-Server**: Clear separation between the client (user interface) and the server (backend logic).
3. **Uniform Interface**: Resources are identified by URIs, and actions are performed using standard HTTP methods.
4. **Layered System**: Components (e.g., proxies, load balancers) can be added between the client and server.

### FastAPI and REST API
- **FastAPI** is a modern, fast (high-performance) Python web framework for building APIs.
- Built on **Starlette** (for web applications) and **Pydantic** (for data validation).
- Implements REST principles efficiently, leveraging Python's type hints and async capabilities.

---

## REST API Components Table

| **Component**        | **Description**                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------|
| **API**              | Application Programming Interface enabling interaction between software applications.            |
| **Protocol**         | HTTP/HTTPS - defines the communication rules between client and server.                          |
| **Methods**          | `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`.                                      |
| **Query Parameters** | Sent in the URL (`?key=value`) to filter, sort, or modify the request behavior.                  |
| **Path Parameters**  | Part of the URL (`/resource/{id}`) to identify a specific resource.                              |
| **Body Parameters**  | Data sent in the body of the request, typically for `POST`, `PUT`, or `PATCH`.                   |
| **Client-Side Errors**| HTTP 4xx status codes, e.g., `400` (Bad Request), `401` (Unauthorized), `404` (Not Found).      |
| **Server-Side Errors**| HTTP 5xx status codes, e.g., `500` (Internal Server Error), `503` (Service Unavailable).        |
| **Successful**       | HTTP 2xx status codes, e.g., `200` (OK), `201` (Created), `204` (No Content).                    |
| **Redirection**      | HTTP 3xx status codes, e.g., `301` (Moved Permanently), `302` (Found).                           |

---

## Authentication Methods

### 1. **Basic Authentication**
- **Description**: Sends a username and password encoded as base64 in the `Authorization` header.
- **Header Example**: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
- **Use Case**: Simple and easy to implement but less secure unless combined with HTTPS.

### 2. **OAuth 1.0**
- **Description**: Provides a secure way for applications to access user data without exposing passwords. Uses signatures to verify requests.
- **Components**:
- `Consumer Key` and `Secret`
- Request Tokens and Access Tokens
- **Use Case**: Preferred for highly secure data transactions (e.g., financial data).

### 3. **OAuth 2.0**
- **Description**: Token-based authentication for access delegation. More flexible than OAuth 1.0.
- **Grant Types**:
- `Authorization Code`
- `Implicit`
- `Password`
- `Client Credentials`
- **Use Case**: Widely used for web and mobile applications (e.g., Google, Facebook logins).

### 4. **JSON Web Tokens (JWT)**
- **Description**: Compact, self-contained tokens for secure data exchange between parties.
- **Structure**: Three parts separated by dots (`.`):
1. **Header**: Contains token type and signing algorithm.
2. **Payload**: Contains claims like user info and expiration time.
3. **Signature**: Verifies the token's integrity.
- **Example**:
```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiZXhwIjoxNjIzMjQ3OTQwfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```
![carbon](https://github.com/user-attachments/assets/f65366f6-d62d-4092-acea-2e6f302f5dd6)


# HTTP Status Codes

| **Code** | **Category**           | **Description**                                                                            |
|----------|-------------------------|--------------------------------------------------------------------------------------------|
| **1xx**  | **Informational**       | The request was received, continuing process.                                              |
| **100**  | Continue                | The client can continue with its request.                                                 |
| **101**  | Switching Protocols     | The server is switching protocols as requested by the client.                             |
| **102**  | Processing              | The server has received and is processing the request, but no response is yet available.  |
| **103**  | Early Hints             | Provides hints to help the client start preloading resources.                             |
| **2xx**  | **Successful**          | The request was successfully received, understood, and accepted.                          |
| **200**  | OK                      | Standard response for successful requests.                                                |
| **201**  | Created                 | Resource successfully created.                                                            |
| **202**  | Accepted                | The request has been accepted for processing, but the processing is not complete.         |
| **203**  | Non-Authoritative Info  | Response received from another source, not authoritative.                                 |
| **204**  | No Content              | The server successfully processed the request but is not returning any content.           |
| **3xx**  | **Redirection**         | Further action needs to be taken by the client to complete the request.                   |
| **301**  | Moved Permanently       | The resource has been moved to a new URL permanently.                                     |
| **302**  | Found                   | Temporary redirection to a different URL.                                                |
| **307**  | Temporary Redirect      | Redirects to a different URL but with the same method.                                    |
| **308**  | Permanent Redirect      | Permanent redirect with the same method.                                                 |
| **4xx**  | **Client Errors**       | The client sent an invalid request or is not authorized.                                  |
| **400**  | Bad Request             | The request is malformed or cannot be fulfilled.                                          |
| **401**  | Unauthorized            | Authentication is required but was not provided.                                          |
| **402**  | Payment Required        | Reserved for future use (originally for digital payments).                                |
| **403**  | Forbidden               | The server understands the request but refuses to authorize it.                           |
| **404**  | Not Found               | The server cannot find the requested resource.                                            |
| **405**  | Method Not Allowed      | The method is not allowed on the target resource.                                         |
| **5xx**  | **Server Errors**       | The server encountered an error or is unable to fulfill the request.                      |
| **500**  | Internal Server Error   | A generic error occurred on the server.                                                  |
| **501**  | Not Implemented         | The server does not support the functionality required to fulfill the request.            |
| **502**  | Bad Gateway             | The server received an invalid response from an upstream server.                          |
| **503**  | Service Unavailable     | The server is overloaded or down for maintenance.                                         |
| **504**  | Gateway Timeout         | The server did not receive a timely response from an upstream server.                     |
| **505**  | HTTP Version Not Supported | The server does not support the HTTP protocol version used in the request.             |


