# Installation & Prerequisites
The project can be started on all common operating systems by using Docker. Manual execution with Python is possible in these early stages.
## Docker and Compose
Install [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/).
## Building
1. Create the environment file ``.env`` by copying and renaming ``.env.example``.
2. Configure the ``.env`` file.
3. Build the project by running:<br>
   `` docker-compose build ``<br>
4. Run the project:<br>
   `` docker-compose run ``<br>