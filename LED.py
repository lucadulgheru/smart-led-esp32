from constants import LED_STATUS_ON, LED_STATUS_OFF

class LED:
    def __init__(self, led_id, led_status, led_color, neopixel):
        self.led_id = led_id
        self.led_status = led_status
        self.led_color = led_color
        self.neopixel = neopixel
        
    def toggle(self):
        if self.led_status == LED_STATUS_ON:
            self.led_status = LED_STATUS_OFF
            self.neopixel[self.led_id] = (0, 0, 0)
            self.neopixel.write()
        else:
            self.led_status = LED_STATUS_ON
            self.neopixel[self.led_id] = self.led_color
            self.neopixel.write()
    
    def change_color(self, led_color):
        self.led_color = led_color
        self.neopixel[self.led_id] = self.led_color
        self.neopixel.write()
        
    def led_info(self):
        return {
                "id": self.led_id,
                "status": self.led_status,
                "color": self.led_color
            }
        
    