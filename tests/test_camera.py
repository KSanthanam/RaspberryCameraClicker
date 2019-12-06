import sys
import fake_rpi
import time

sys.modules['RPi'] = fake_rpi.RPi

try:
    from RPi.GPIO import GPIO
except:
    import RPi as RPi
    GPIO = RPi.GPIO

from CameraClicker.Camera import Camera
stack = []

@pytest.mark.parametrize('port', [(1), (3)])     
class TestCamera():
  def test_port(self, port):
    camera = Camera(port=port)
    assert camera.usb_port() == port
