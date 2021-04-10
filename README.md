# About

A single blood sample taken from a person has many T-cells in it.  Each T-cell has RNA in it.  Each RNA strand has a CDR3 sequence in it.  From the sample we record which CDR3 sequences occur and the frequency of each one.  This data is called the **TCR repertoire** (T-cell receptor repertoire) of the sample.

Given two separate samples, we can define a **distance** between them.  In the file `sample_distances.py` you can see various distance functions that we are experimenting with (so far we have the `l2` distance (Euclidean), the `jaccard` distance, and the `weighted_jaccard` distance).

The goal of this repo is to use metrics to evaluate how good these distance functions are, as well as perform other TCR analysis.




## Install

Install [Docker](https://www.docker.com/get-started).  That's it!



## Run dev environment

    docker-compose up --build

then visit `http://localhost:4001/?token={entertokenhere}`.  You should see a Jupyter frontend.



## Test dev

To run tests, run the dev environment (see above) and then (in a separate terminal window):

	docker exec -it tcr-analysis-container bash
	pytest



## build, test, and deploy
The server is a dev server

	git push
	docker push mvlancellotti/tcr-analysis:dev
	ssh date
	tmux
	cd tcr-analysis
	git pull
	docker pull mvlancellotti/tcr-analysis:dev
	sudo docker-compose up --build

then visit `date:4001` or `http://date:4001/notebooks/cdr3_lifespan.ipynb?token={entertokenhere}`.
