FROM python:3.10 as py3
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
RUN pip install flask \ 
    pip install gunicorn \ 
    python-math \
    requests_html

RUN mkdir /app
COPY ./Cur_Ctr.py /app/Cur_Ctr.py
COPY ./Mod_Ctr.py /app/Mod_Ctr.py
WORKDIR /app
# CMD [ "python3", "-u", "./Cur_Ctr.py" ]
CMD ["gunicorn","-b",  "0.0.0.0:6003", "Cur_Ctr:app"]