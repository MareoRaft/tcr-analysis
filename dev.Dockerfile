# Please update versions once every 6 months
FROM jupyter/scipy-notebook:4d9c9bd9ced0

WORKDIR /home/matt/work

RUN pip3 install Distance==0.1.3
RUN pip3 install colorlog==4.7.2
RUN pip3 install ngram==3.3.2
RUN pip3 install pytest==6.0.1

CMD ["jupyter", "notebook"]
