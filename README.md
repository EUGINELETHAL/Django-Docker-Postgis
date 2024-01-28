# Dockerizing Django with Postgres(Postgis), Gunicorn, and Nginx

## Want to learn how to build this?



## Want to use this project?
Some features of this project:

Uses GeoDjango, so needs GDAL etc for the Django app plus a PostgreSQL server running PostGIS
Already has a Dockerfile used for the production deployment, but needed a separate one for the development environment
The db container runs PostGIS. It uses a named volume to persist PostgreSQL data in between container restarts.

The dev web container runs the Django development server, built using   Dockerfile while the production web contianer is built using the custom Dockerfile.prod Dockerfile


### Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.
    ```sh
    $ docker-compose up -d --build
    ```
   

### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
