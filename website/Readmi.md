Sign Up
http://localhost:8000/users/sign_up
  
  - username
  - first_name
  - last_name
  - email
  - password
  
Sign In
http://localhost:8000/users/sign_in
  
  - email
  - password
  
  * response : ( token )
  
Timeline
http://localhost:8000/status/

Post Status
http://localhost:8000/status/post/

  - message
  
  - Headers = { token: '' }

Edit Status
http://localhost:8000/status/update/<status-id>/

  - message
  
  - Headers = { token: '' }
  
Delete Status
http://localhost:8000/status/delete/<status-id>/

  - Headers = { token: '' }
  
Add comment status
http://localhost:8000/status/comment/<status-id>/

  - comment
  
  -Headers = { token: '' }