# PSET 2 Learning Status Codes
## Memorize the three main categories 2xx, 4xx, 5xx
### 2xx(Success), 4xx(Client Error), 5xx(Server Error)

| Scenario | Recommended Status Code |
| :--- | :--- |
| User sends GET /routines. You find 10 routines and return them. | 200	|
| User sends POST /routines. You successfully save it to the DB. | 201 |
| User sends GET /routines/999. ID 999 does not exist in the DB. | 404 |
| User sends POST /routines but forgets the "name" field. (Pydantic catches this). | 422 |
| User sends DELETE /routines/5. You are not logged in. | 401 |
| Your database cable gets unplugged while trying to save data. | 500 |