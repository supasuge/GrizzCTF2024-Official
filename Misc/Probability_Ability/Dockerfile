FROM python:3.10-alpine

# create a user to run the app
RUN adduser -D appuser

# set working directory to /app
WORKDIR /app

# copy server.py, ans.txt, and flag.txt files into the working directory
COPY server.py ans.txt flag.txt /app/

# change ownership to the new user
RUN chown -R appuser:appuser /app

USER appuser

# expose port 9999 for the challenge.
EXPOSE 9999

# run the python server (challenge)
CMD ["python", "server.py"]


# Buidl the docker image
# docker built -t quiz-challenge .
# docker run --name quiz-challenge -p 9999:9999 -d quiz-challenge

# Viewing the logs
# docker logs quiz-challenge-container
