## A simple URL Shortener written with fastapi. 
* Using a simple SQLite database and redis as a cache to improve performance.
* For creating short url I used hashing with resolving collision by checking database before saving but we can also use
base N algorithm instead. 
* I added sentry to log errors and check performance issues, etc. But unfortunately I didn't have a server so I had to
commented it out.