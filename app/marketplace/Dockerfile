FROM node:latest
ADD . /marketplace/
WORKDIR /marketplace
RUN cd /marketplace
RUN npm install \
    cache clean
EXPOSE 8545 3000
COPY ./run.sh run.sh
RUN chmod +x run.sh
# ENTRYPOINT ./run.sh
CMD ./run.sh