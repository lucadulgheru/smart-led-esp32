from constants import LED_STATUS_OFF
from LED import LED
from request_handler import handle_request

led_list = [LED(x, LED_STATUS_OFF, (255, 255, 255), neopixel_strip) for x in range(10)]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    handle_request(conn, addr, led_list)
