# About

A single blood sample taken from a person has many T-cells in it.  Each T-cell has RNA in it.  Each RNA strand has a CDR3 sequence in it.  From the sample we record which CDR3 sequences occur and the frequency of each one.  This data is called the **TCR repertoire** (T-cell receptor repertoire) of the sample.

Given two separate samples, we can define a **distance** between them.  In the file `sample_distances.py` you can see various distance functions that we are experimenting with (so far we have the `l2` distance (Euclidean), the `jaccard` distance, and the `weighted_jaccard` distance).

The goal of this repo is to use metrics to evaluate how good these distance functions are, as well as perform other TCR analysis.




## Install

Install [Docker](https://www.docker.com/get-started).  That's it!



## Run dev environment

    docker-compose up --build

then visit `localhost:4001` or `http://localhost:4001/notebooks/analysis.ipynb?token={entertokenhere}`.  You should see a Jupyter frontend.



## Test dev

To run tests, run the dev environment (see above) and then (in a separate terminal window):

	docker exec -it tcr-analysis-container bash
	pytest



## build, test, and deploy
The server is a dev server

  # todo: once the below is reliable, move it into a script so it can be fully automated
  git push
  docker push mvlancellotti/tcr-analysis:dev
  ssh date
  # if it says 'System restart required', restart the machine
  sudo reboot
  su matt
  tmux
  # reattach to 'tcr-analysis' tmux session
  cd tcr-analysis
  # commit changes if biologist made any meaningful changes, otherwise just throw them out
  git checkout -- .
  git pull
  sudo docker pull mvlancellotti/tcr-analysis:dev
  # consider deleting old images if the droplet runs out of space
  # use ctrl-C to exit current container
  # remove the container if necessary
  sudo docker rm tcr-analysis-container
  # ALL docker commands including this one are not necessary if you didn't make docker changes
  sudo docker-compose up --build

then visit `date:4001` or `http://date:4001/notebooks/analysis.ipynb?token={entertokenhere}`.
