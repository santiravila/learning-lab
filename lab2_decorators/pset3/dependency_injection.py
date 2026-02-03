"""
Implement a rudimentary Dependency Injection to better understand how FastAPI loads resources
"""

class MockDB():
    def get_data(self):
        return ["Routine1", "Routine2"]
    

def get_db_session():
    return MockDB()


# NOT global state (hidden dependency) NOR coupling (internal creation). Instead passing state as parameter (DI)
def list_routines(db: MockDB):
    return db.get_data()


def simulate_fastapi_request(endpoint_function, dependency_provider):
    resource = dependency_provider()
    return endpoint_function(resource)


print(simulate_fastapi_request(list_routines, get_db_session))