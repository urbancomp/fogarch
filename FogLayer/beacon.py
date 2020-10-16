class Beacon:
    # pass
    # Header = ""
    # Id     = 0
    # Velo   = 0.0
    # Road   = ""
    # PosX   = ""
    # PosY   = ""
    # STime  = 0.0
        
    def __init__(self,  _Header, _Id, _Velo, _Road, _PosX, _PosY, _STime, _Timer, _Slot):
        self.Header = _Header
        self.Id = _Id
        self.Velo = _Velo
        self.Road = _Road
        self.PosX = _PosX
        self.PosY = _PosY
        self.STime = _STime
        self.Timer = _Timer
        self.Slot = _Slot
        
  
    def newCar(self):
         print ("Engine started")

    