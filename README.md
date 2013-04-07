Matrix - The Application Repository
======================================

Centralized repository for application management which are under development or running in production. Inform dependencies of the project; components, services and most importantly people. Display errors, logs, messages, status, some metrics of the application quickly. 

Features
------------
* API


Integration Ideas
--------------
- Github
- Sentry
- NewRelic
- Munin
- Jenkins

Ideas
------------

- Spec ( Features ) display.. Read the tests folder, figure out what features are implemented
- Find project dependencies. ( Requirements.txt ) and search import statements
- **Status pages** -> For each application environment, display the status page of the project  -- Each project must implement the /status page as a HTML/JSON page.
-- Current running codebase
-- Up and running
-- Memory consumption of instances


- Application Dashboard ( Channel in some metrics ) https://github.com/evolvedlight/pydashie
- Latest error logs Loggly or whatever.Sentry!!
- JIRA Tickets
- Github issues
- Confluence Pages
- Jenkins Integration ( Deploying latest version, latest build failed, etc.. )

