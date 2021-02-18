# Picking a distance to compare TCR data across patients

  1. pick 1 metric to say how "good" a distance is
    * accuracy
    * if the model, given a sample, guesses which patient it is, then we can run LOOCV and report the percentage of inputs that had the correct output
  2. pick 1 distance
    * hamming distance.  # of disagreeing letters (between 2 CDR3 alpha sequences)
    * in a tie, choose person w/ highest frequency
  3. Evaluate its goodness
    * the model can be k-nearest neighbors





## Install

To install deps:

	pip3 install -r requirements.txt


## Run

To run:

	pytest
