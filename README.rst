=====
Distance Matrix
=====

Distance Matrix is a simple app that allows to fetch (and cache) distances between N points having an upper limit on number of nodes and edges.

This is achieved by having a matrix, each point if first assigend to a sector and distance between sectors is used.

This compromises the accuracy slightly, but the advantages is huge, as the resource usage is limited,

Library can be set up to fetch road distance from google right away, or, create a placeholder that will be filled by a job later

Quick start
-----------

1. Add "distance_matrix" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'distance-matrix',
    ]

2. Run `python manage.py migrate` to create the polls models.

3. Set up variables in settings.py::

    GOOGLE_API_KEY #google API key for distance matrix
    DISTANCES_RESOLUTION_LNG = 0.141745 #sector height
    DISTANCES_RESOLUTION_LAT = 0.076359 #sector width
    DISTANCES_AVERAGING_KM = 20 #distance averaging

To get distance::

    get_distance(lat1, lng1, lat2, lng2, fetch_now=True)

Run job that fetches unknown distances::

    python manage.py fetch_distances