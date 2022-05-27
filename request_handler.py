import json
from constants import *
from log_handler import log_info, get_logs

def handle_request(connection, address, led_list):
    response_object = parse_request(connection, address, led_list)
    send_response(connection, response_object)

def parse_request(connection, address, led_list):
    request = str(connection.recv(1024))
    if PING_ENDPOINT_BASE_PATH in request:
        return build_ping_response()
    elif ENUMERATION_ENDPOINT_BASE_PATH in request:
        return build_enumeration_response(led_list)
    elif LED_ENDPOINT_BASE_PATH + LED_ACTION_TOGGLE in request:
        led_id = extract_led_id_from_request(request)
        selected_led = next(led for led in led_list if led.led_id == led_id)
        selected_led.toggle()
        log_event_address(EVENT_LED_TOGGLE, address[0])
        return build_led_toggle_response(selected_led.led_id, selected_led.led_status, selected_led.led_color)
    elif LED_ENDPOINT_BASE_PATH + LED_ACTION_COLOR in request:
        led_id = extract_led_id_from_color_change_request(request)
        selected_led = next(led for led in led_list if led.led_id == led_id)
        color = parse_color_from_request(request)
        selected_led.change_color(color)
        log_event_address(EVENT_LED_COLOR_SWITCH, address[0])
        return build_led_toggle_response(selected_led.led_id, selected_led.led_status, selected_led.led_color)
    elif EVENTS_ENDPOINT_BASE_PATH in request:
        return build_events_response()

def send_response(connection, response_object):
    connection.send('HTTP/1.1 200 OK\n')
    connection.send('Content-Type: text/html\n')
    connection.send('Connection: close\n\n')
    connection.sendall(response_object)
    connection.close()

def build_events_response():
    logs = get_logs()
    parsed_logs = [parse_log(log) for log in logs]
    response_object = {
        "log_count": len(logs),
        "logs": parsed_logs
    }
    return json.dumps(response_object)

def build_led_toggle_response(led_id, led_status, led_color):
    response_object = {
        "id": led_id,
        "status": led_status,
        "color": led_color
    }
    return json.dumps(response_object)

def build_ping_response():
    response_object = {
        "message": "Everything's good in the jungle, chief"
    }
    return json.dumps(response_object)

def build_enumeration_response(led_list):
    led_count = len(led_list)
    leds = [led.led_info() for led in led_list]
    response_object = {
        "led_count": led_count,
        "leds": leds
    }
    
    return json.dumps(response_object)

def extract_led_id_from_color_change_request(request):
    print(request)
    print(request[request.find("color") + len("color") + 1: request.find('?')].strip())
    return int(request[request.find("color") + len("color") + 1: request.find('?')].strip())

def extract_led_id_from_request(request):
    return int(request[request.find("toggle") + len("toggle") + 1: request.find('HTTP')].strip())

def parse_color_from_request(request):
    hex_code = request[request.find("color_code") + len("color_code="):]
    print(hex_code)
    r = int(hex_code[:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    
    return (r, g, b)

def parse_log(log):
    log_tokens = log.split("-")
    return {
        "date": log_tokens[0].lstrip().rstrip(),
        "issuer_address": log_tokens[1].lstrip().rstrip(),
        "event_type": log_tokens[2].lstrip().rstrip()
    }

def log_event_address(msg, address):
    log_info(address + " - " + EVENT_LED_TOGGLE)
def log_event(msg):
    log_info(msg)