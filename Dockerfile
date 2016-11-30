FROM python



RUN mkdir -p /usr/cli

WORKDIR /usr/cli

ENTRYPOINT [ "python3", "main.py" ]