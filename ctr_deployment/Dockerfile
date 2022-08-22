FROM python:3.10
RUN pip install flask python-math requests_html gunicorn
RUN mkdir /app
COPY ./ctr_rest_api.py /app
COPY ./Mod_Ctr.py /app
COPY ./ctr.json /app
WORKDIR /app
CMD ["gunicorn", "-b",  "0.0.0.0:5000", "ctr_rest_api:app"]