from constants import LED_STATUS_OFF
from LED import LED
from request_handler import handle_request

led_list = [
        LED(0, LED_STATUS_OFF, "BLUE", led_0)
    ]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    handle_request(conn, addr, led_list)
