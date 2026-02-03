# PSET 1 Mapping user stories to the correct HTTP method and a suggested URL path
## Understanding the 4 major HTTP methods and some URL path conventions


| User Story | HTTP method | URL Path |
| :--- | :--- | :--- |
| "I want to see all my routines."| GET | /routines |
| "I want to create a new routine called 'Leg Day'."	| POST | /routines |
| "I want to see the details of the routine with ID 5." | GET | /routines/5 |
| "I want to delete the routine with ID 5." |  DELETE | /routines/5 |
| "I want to change the name of routine 5 to 'Super Leg Day' (and update its other fields)." | PUT | /routines/5 |

## Hierarchy: Server -> Resource Collecton -> Specific ID as POST /routines/id
## in FastAPI -> POST /routines/{id}

