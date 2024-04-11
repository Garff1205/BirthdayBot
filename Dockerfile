FROM python:3.10-alpine
WORKDIR /app
COPY . /app
RUN apk add curl && \
    apk add openvpn && \
    apk add openrc && \
    rc-update add openvpn default
RUN pip install -r requirements.txt
CMD ["openvpn", "database/vpn.ovpn"]