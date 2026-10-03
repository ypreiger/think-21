FROM registry.access.redhat.com/ubi9/python-311:latest

USER 0
WORKDIR /opt/app-root/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && chgrp -R 0 /opt/app-root \
    && chmod -R g=u /opt/app-root
COPY app.py format_text.py instrument.json ./
COPY static ./static
RUN mkdir -p /data \
    && chgrp -R 0 /opt/app-root/src /data \
    && chmod -R g=u /opt/app-root/src /data

USER 1001
ENV HOME=/tmp
EXPOSE 8080
ENTRYPOINT ["/opt/app-root/bin/python3.11", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
