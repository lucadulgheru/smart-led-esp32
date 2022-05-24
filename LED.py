from constants import LED_STATUS_ON, LED_STATUS_OFF

class LED:
    def __init__(self, led_id, led_status, led_color, pin):
        self.led_id = led_id
        self.led_status = led_status
        self.led_color = led_color
        self.pin = pin
        
    def toggle(self):
        if self.led_status == LED_STATUS_ON:
            self.led_status = LED_STATUS_OFF
            self.pin.value(0)
        else:
            self.led_status = LED_STATUS_ON
            self.pin.value(1)
    
    # TODO add actual color change logic -> set/unset required bits
    def change_color(self, led_color):
        self.led_color = led_color
        
    def led_info(self):
        return {
                "id": self.led_id,
                "status": self.led_status,
                "color": self.led_color
            }
        
    