# Django Application User

## Authorization
Create new user
```python
import uuid
username = str(uuid.uuid4())[0:18]
password = str(uuid.uuid4())
print({"username":username, "password":password})
```
## Current username and password
* Username: xxxx
* Password: xxxx
