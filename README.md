# Adonai Client

Client for [Adonai](https://github.com/Egnod/adonai) server based on [SGQLC](https://github.com/profusion/sgqlc) with code-generated types and queries


# Use Examples

### Create client instance
```python
from adonai_client import AdonaiClient, QueryType

client = AdonaiClient("http://localhost:5000", username="admin", password="admin")
```
###  Query Example with Field selection

```python
query = client.query() # Query instance
permissions_query = query.permissions() # Query name selection

print(query)
```
Query string:
```
query {
  permissions {
    createdAt
    updatedAt
    projectId
    name
    description
    type
    isActive
    id
    project {
      createdAt
      updatedAt
      domainId
      name
      uuid
      description
      isActive
      id
    }
  }
}
```

Select only id and name fields from permissions query and project sub-selection if project not null:
```python
client.fields(permissions_query, id=True, name=True)
client.fields(permissions_query.project(), id=True, name=True)

print(query)
```

Current query:
```bash
query {
  permissions {
    id
    name
    project {
      id
      name
    }
  }
}
```

Execute query:
```python
permissions = client.execute(query)

print(permissions)
```
Result:
```bash
   {'permissions': [{'id': '1', 'name': 'domain_read', 'project': None},
   {'id': '2', 'name': 'domain_create', 'project': None},
   {'id': '3', 'name': 'domain_delete', 'project': None},
   {'id': '4', 'name': 'domain_update', 'project': None},
....
   {'id': '29', 'name': 'test_permission_1', 'project': {'id': '1', 'name': 'test_project'}},
   {'id': '30', 'name': 'test_permission_2', 'project': {'id': '1', 'name': 'test_project'}}]}
```

###  Multi-Query Example with exclude fields

```python
query = client.query() # Query instance
projects_query = query.projects() # Query name selection
users_query = query.users()

client.fileds(projects_query, domains=False, permissions=False)
client.fields(users_query, domain=False, groups=False, permissions=False, internal_permissions=False)

print(query)
```

```bash
query {
  projects {
    createdAt
    updatedAt
    domainId
    name
    uuid
    description
    isActive
    id
  }
  users {
    createdAt
    updatedAt
    domainId
    login
    uuid
    firstName
    lastName
    internalAuth
    isActive
    id
  }
}
```
Execution result:
```bash
{'projects': [{'createdAt': '2020-01-18T01:53:51.976311',
    'updatedAt': '2020-01-18T02:09:03.791269',
    'domainId': 5,
    'name': 'test',
    'uuid': '7abf87a2-66f0-4924-89bc-142cd03127e6',
    'description': 'test',
    'isActive': True,
    'id': '1'}],
  'users': [
   {'createdAt': '2020-01-18T22:53:38.728965',
    'updatedAt': None,
    'domainId': 6,
    'login': 'test',
    'uuid': '05f283e4-7938-41ea-bb99-112fc6595670',
    'firstName': 'test',
    'lastName': 'test',
    'internalAuth': False,
    'isActive': True,
    'id': '10'}]}
```

### Mutation example

Create mutation and select from domain id and uuid fields

```python
mutation = client.mutation()
create_domain_mutation = mutation.create_domain(name="test_domain", description="Domain for tests")

client.fields(create_domain_mutation.domain(), id=True, uuid=True)

print(mutation)
```
Mutation query:
```bash
mutation {
  createDomain(name: "test_domain", description: "Domain for tests") {
    domain {
      id
      uuid
    }
  }
}
```
Execution:
```python
domain = client.execute(mutation)

print(domain)
```
```bash
{'createDomain': {'domain': {'id': '8',
   'uuid': 'eb8738e3-9b28-4acb-8a20-85b7c5c3f9b9'}}}
```