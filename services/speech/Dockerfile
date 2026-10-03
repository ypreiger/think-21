FROM registry.access.redhat.com/ubi9/python-311:latest

USER 0
RUN dnf install -y libgomp && dnf clean all
WORKDIR /opt/app-root/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && chgrp -R 0 /opt/app-root \
    && chmod -R g=u /opt/app-root
COPY app.py .
RUN chgrp -R 0 /opt/app-root/src && chmod -R g=u /opt/app-root/src

USER 1001
ENV HOME=/tmp \
    HF_HOME=/models \
    XDG_CACHE_HOME=/models
EXPOSE 8080
ENTRYPOINT ["/opt/app-root/bin/python3.11", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
