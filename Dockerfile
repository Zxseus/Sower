FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/zxseus/Sower /home/sower/ \

    && chmod 777 /home/sower \

    && mkdir /home/sower/bin/

COPY ./sample_config.env ./config.env* /home/sower/

WORKDIR /home/sower/

CMD ["python3", "-m", "userbot"]
