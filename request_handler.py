import json
from constants import *

def handle_request(connection, address):
	# TODO do sth with the address, will ya?
	response_object = parse_request(connection, address)
	send_response(connection, response_object)

# We need to search for the "endpoint" which is being called
def parse_request(connection, address):
	request = str(connection.recv(1024))
	if PING_ENDPOINT_BASE_PATH in request:
		return build_ping_response()
	elif ENUMERATION_ENDPOINT_BASE_PATH in request:
		return build_enumeration_response()
	elif LED_ENDPOINT_BASE_PATH + LED_ACTION_ON in request:
		# TODO get this shit done plz
		return build_led_toggle_response(0, LED_STATUS_ON)
	elif LED_ENDPOINT_BASE_PATH + LED_ACTION_OFF in request:
		# TODO get this shit done plz
		return build_led_toggle_response(0, LED_STATUS_OFF)

def send_response(connection, response_object):
	conn.send('HTTP/1.1 200 OK\n')
	conn.send('Content-Type: text/html\n')
	conn.send('Connection: close\n\n')
	conn.sendall(response_object)
	conn.close()

def build_led_toggle_response(led_id, led_status):
	response_object = {
		"id": led_id,
		"status": led_status
	}
	return json.loads(response_object)

def build_ping_response():
	response_object = {
		"message": "Everything's good in the jungle, chief"
	}
	return json.loads(response_object)

def build_enumeration_response():
	response_object = {
		# TODO complete here
		"led_count": 0
	}
