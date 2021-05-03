# Please update versions once every 6 months
FROM jupyter/scipy-notebook:4d9c9bd9ced0

WORKDIR /home/jovyan/work

# install deps
RUN pip3 install Distance==0.1.3
RUN pip3 install colorlog==4.7.2
RUN pip3 install ngram==3.3.2
RUN pip3 install pytest==6.0.1

# set password
RUN sed -i 's/# c\.NotebookApp\.password = '"''"'/c.NotebookApp.password = '"'"'argon2:$argon2id$v=19$m=10240,t=10,p=8$ADIG2a9omJPQTlVTfSvlZA$gmBX7zFr59lWfas8W6YeFw'"'"'/' /home/jovyan/.jupyter/jupyter_notebook_config.py

CMD ["jupyter", "lab"]
