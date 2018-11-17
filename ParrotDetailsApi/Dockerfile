FROM python:3
ENV PYTHONUNBUFFERED 1
RUN pip install flask \
	flask_restful
ENV entrypoint=/api/main.py
COPY  src /api
CMD python ${entrypoint}