=====
Distance Matrix
=====

Distance Matrix is a simple app that allows to fetch (and cache) distances between N points having an upper limit on number of nodes and edges.

This is achieved by having a matrix, each point if first assigend to a sector and distance between sectors is used.

This compromises the accuracy slightly, but the advantages is huge, as the resource usage is limited,

Quick start
-----------

1. Add "distance_matrix" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'distance-matrix',
    ]

2. Run `python manage.py migrate` to create the polls models.

