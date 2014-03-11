Photo-Z analysis GUI
====================

# Prerequisite

+ numpy
+ scipy
+ matplotlib
+ Tkinter

# Configuration

The configure file is needed in *sparameter.py*

The important requirements following:

## CMR

Specify the color magnitude relation

## Galaxy catalog

The galaxies for each cluster are stored in a file specified by the cluster ID



## Database

The database is build to store the information of each cluster candidate
First time run:

    python accessDB.py


The following command are used to create a database from cluster catalog *catalog.dat*

    db = Candidate()
    db.create_from_catalog("catalog.dat")
    db.create_comment()
    for method in P_method:
        db.update_method("all", method)

It create a *DB_FILE* contains:

+ DB_cat for main catalog
+ DB_PZ for photo-z comment
+ all clusters under each method table in P_method

## Photo-z analysis result

This is post-processed result for photozMVC.py
The result is stored at ./result/run/pz*ID*_?_bg.dat
Notice, the *run* is specified by p_method

# Cluster FITS image and position/CMR plot

    python galcontrol

## Functions

+ Select galaxies in sketch and create new catalog based on selection

+ Create color magnitude plot and show the distribution of given color range objects on sky

+ Save region files of selections

+ call ds9 to view FITS image

# Cluster Photo-z result display

    python photozMVC.py

## Functions

+ Show the result of photo-z analysis

+ fit the P(z) with Gaussian curve with sigma-clipping