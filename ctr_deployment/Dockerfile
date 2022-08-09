FROM python:3.10
RUN pip install flask python-math requests_html
RUN mkdir /app
COPY ./ctr_rest_api.py /app
COPY ./Mod_Ctr.py /app
COPY ./ctr.json /app
WORKDIR /app
CMD ["python3", "./ctr_rest_api.py"]