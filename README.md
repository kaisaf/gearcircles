# GearCircles

GearCircles is a person-to-person gear rental marketplace for outdoor sports. It
connects the local gear owners to those eager to try new things. 

GearCircles is a Django project build on top of:
* [GeoDjango] (http://geodjango.org/)
* [PostGIS] (http://postgis.net/)
* [Google Identity Toolkit] (https://developers.google.com/identity/toolkit/)
* [Google Maps] (https://developers.google.com/maps/)
* [PayPal Adaptive Payments] (https://developer.paypal.com/docs/classic/adaptive-payments/integration-guide/APIntro/)
* [Django REST framework] (http://www.django-rest-framework.org/)
* [Twilio] (https://www.twilio.com/)

Users sign in through their existing Google, Microsoft or Facebook accounts. They
can search gear near them based on categories, price ranges, dates or search words.
Gear owners can list their equipment using category specific forms and accept
PayPal or cash payments.

Deployment
===========

Dependent on kartoza/postgis

Pull the latest postgis image

`docker pull kartoza/postgis`

Start the postgis container with the name `postgis`. Note the `-v` tag - this stores the postgres data on the host system (in `/gears/postgres_data`) rather than inside the container. This is important because if you deleted the `postgis` container at any point, all your data would be deleted with it. This way, it is stored on the host system and you can back it up if necessary.

`docker run --name postgis -dt -v /gears/postgres_data:/var/lib/postgresql -p 25432:5432 kartoza/postgis`

Create the DB inside the container and create the postgis extension. You must have `postgresql-client` installed on the host. Username and password are `docker` and `docker` by default.

`createdb gearcircles -h localhost -U docker -p 25432`

`psql -h localhost -U docker -p 25432 -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" gearcircles`

Build your project, inside the `gc_project` directory containing `Dockerfile`

`docker build -t gearcircles .`

To migrate the database

`docker run -dit --link postgis:POSTGIS --name migrate gearcircles python3 manage.py migrate`

To run the seeds

`docker run -dit --link postgis:POSTGIS --name seeds gearcircles python3 seeds.py`

To start the server

`docker run -dit --link postgis:POSTGIS --name gearcircles gearcircles`

Run [nginx-proxy](https://github.com/jwilder/nginx-proxy)

`docker run -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro jwilder/nginx-proxy`

Some useful Docker commands:

Check the running containers: `docker ps`

Check recently exited containers: `docker ps -l`

Look at the output of a container (for example `nginx-proxy` contains all your network traffic): `docker logs [container name]`

Kill a container: `docker kill [container name]`

Remove a container: `docker rm [container name]`

See all docker images available: `docker images`

Remove an image `docker rmi -f [image name]`


Developers:
* Kaisa Filppula
* Victor Menezes
