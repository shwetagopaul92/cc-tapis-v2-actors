# pull base image
FROM {{ cookiecutter.docker_base_repo }}

# add requirements.txt to docker container
ADD requirements.txt /requirements.txt

# install requirements.txt
RUN pip3 install -r /requirements.txt

# add the python script to docker container
ADD default.py /default.py

# command to run the python script
CMD ["python", "/default.py"]
