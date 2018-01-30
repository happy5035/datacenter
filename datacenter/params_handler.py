# -*- coding: utf-8 -*-
import json
import socket


def client(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    return sock


def send_params(params):
    sock = client('localhost', 8088)
    sock.send(bytes(json.dumps(params), encoding='utf-8'))

    pass
