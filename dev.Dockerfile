FROM jupyter/scipy-notebook

WORKDIR /home/matt/work

RUN pip3 install ujson
RUN pip3 install pytest
RUN pip3 install ediblepickle
RUN pip3 install spacy==2.2.3
RUN python3 -m spacy download en

CMD ["sleep", "999999"]
