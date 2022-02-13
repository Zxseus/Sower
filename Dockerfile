FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/MatrixBotz/Zeployman /home/zeployman/ \
    && chmod 777 /home/zeployman \
    && mkdir /home/zeployman/bin/

WORKDIR /home/zeployman/

CMD [ "bash", "start" ]
