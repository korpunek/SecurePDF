FROM python:3.11

RUN python3 -m venv /opt/venv

# Install dependencies:
COPY requirements.txt .

RUN /opt/venv/bin/pip install -r requirements.txt

# Run the application:
COPY SecurePDF .

CMD ["/opt/venv/bin/python", "app.py"]