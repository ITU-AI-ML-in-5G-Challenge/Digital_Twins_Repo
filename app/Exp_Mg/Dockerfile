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
COPY ./Exp_Mg.py /app/Exp_Mg.py
COPY ./Mod_Ctr.py /app/Mod_Ctr.py
WORKDIR /app
# CMD [ "python3", "-u", "./Exp_Mg.py" ]
CMD ["gunicorn", "-b",  "0.0.0.0:6001", "Exp_Mg:app"]