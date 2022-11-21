![alt text](./img/SQLModel.png)

## FastAPI + SQLModel Boilerplate App

A RestAPI real world app based on SQLModel [documentation example](https://sqlmodel.tiangolo.com/tutorial/), using [FastAPI](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/)

### Quickstart

1.  <b>Start the App</b>:

- Using Python:
  `docker-compose up -d --build`

- sing Docker:
  `docker build -t sqlmodel-api:latest . && docker run -p 8080:8080 sqlmodel-api:latest`

2. <b>Use Openapi at</b>: `http://localhost:8080/#/`

### Running Tests:

While your app is running, open another terminal:
`pytest -v tavern_tests/`

![alt text](./img/SQLModelAPI_openapi.png)

### Some Sample code

```
creates a lawyer:
@pytest.mark.parametrize(
"lawyer_kwargs, lawyer_created",
[
({}, True),
({"email": "invalid@gmail.com "}, True), # note the extra space at the end
({"email": "invalid @gmail.com"}, False), # note the extra space
({"email": "invalid"}, False)],
)
def test_create_lawyer(
session: Session, client: TestClient, lawyer_kwargs: Dict, lawyer_created: bool
):
"""Test lawyer is created."""
LawyerFactory.create()

default_payload = LawyerBaseFactory.build().dict()
kwargs = default_payload | lawyer_kwargs

response = client.post("/lawyers", json=kwargs)

# Assert
assert response.status_code == (200 if lawyer_created else status.HTTP_422_UNPROCESSABLE_ENTITY)

assert len(session.exec(select(Lawyer)).all()) == (2 if lawyer_created else 1)
if lawyer_created:
for key, expected_value in kwargs.items():
if isinstance(expected_value, str):
expected_value = expected_value.strip()
assert response.json()[key] == expected_value
```
