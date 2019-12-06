import time

class Camera(object):
  # def __init__(self):
  def __init__(self, **kwargs):    
    """ Camera()
            The Camera class.
            Please always use *kwargs* in the constructor.
            """
    super(Camera, self).__init__()
    self._on = True
    
