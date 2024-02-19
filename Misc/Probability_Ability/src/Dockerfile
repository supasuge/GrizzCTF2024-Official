FROM python:3.10-slim  

# Create a non-root user for better security
RUN adduser -D appuser

WORKDIR /app

COPY server.py ans.txt flag.txt /app/

USER appuser

EXPOSE 9999

CMD ["python", "server.py"]


# Buidl the docker image
# docker built -t quiz-challenge .
# docker run --name quiz-challenge -p 9999:9999 -d quiz-challenge

# Viewing the logs
# docker logs quiz-challenge-container
