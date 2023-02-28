import visca_over_ip
import time
import logger


'''
    Maps a value between min and max size
        limits(110, 0, 100) -> 100
        limits(-10, 0, 100) -> 0
        limits(50, 0, 100) -> 50
'''
def limits(value, min_value, max_value):
    if value > max_value:
        return max_value
    if value < min_value:
        return  min_value
    return value


class Camera:
    def __init__(self, string_ip):

        self.cam = visca_over_ip.Camera(string_ip)
        self.log = logger.Logger()

        self._int_x : int = 0
        self._int_y : int = 0
        self._int_velX :int = 0
        self._int_velY : int= 0
        self._float_velX : float = 0.0
        self._float_velY : float = 0.0
        self._float_accelerationX :float = 0.0
        self._float_accelerationY :float = 0.0
        self._float_breakingAcceleration :float = 0.0 # breaking acceleration when button is released
        self._int_velMax :int = 24

        self._float_velZoom : float = 0.0
        self._float_accelerationZoom : float = 0.0
        self._float_breakingZoom : float = 0.0
        self._int_velZoom : int = 0 

        #internal time attribue
        self.__float_lastUpdateTime = time.time()




    def update(self):
        float_currentTime = time.time()
        float_deltaTime = float_currentTime - self.__float_lastUpdateTime # 

#         self.log.topic(f'\
# currentTime : {float_currentTime} | deltaTime : {float_deltaTime} | lastTime : {self.__float_lastUpdateTime} \
# int_vel_X : {self._int_velX} | int_vel_y : {self._int_velY} | \
# float_velx : {self.vel_x} | float_vel_y : {self.vel_y} | \
# acc_x : {self.acceleration_x} | acc_y : {self.acceleration_y} | \
# breaking : {self.breaking}'
#         )

        # PAN TILT UPDATE ===========================================================================================================================
        int_accelerationBust = 4 # this variable regulates the acceleration slope (empirical decision)
        int_breakingBust = 5 # this variable regulates the breaking slope (empirical decision)
        if self._float_breakingAcceleration != 0: #breaking velocity update
            if self._int_velX != 0:
                int_accelerationSignalX = 1 if self._float_velX < 0 else -1
                self._float_velX = self._float_velX + int_accelerationSignalX*(self._float_breakingAcceleration*float_deltaTime)*int_breakingBust
            if self._int_velY != 0:
                int_accelerationSignalY = 1 if self._float_velY < 0 else -1
                self._float_velY = self._float_velY + int_accelerationSignalY*(self._float_breakingAcceleration*float_deltaTime)*int_breakingBust
            
            if self._int_velX == 0 and self._int_velY == 0: #when everything is stopped
                 self._float_breakingAcceleration = 0
            
        else: # acceleration velocity update 
            self._float_velX = limits(self._float_velX + (self._float_accelerationX*float_deltaTime)*int_accelerationBust, -self._int_velMax, self._int_velMax)
            self._float_velY = limits(self._float_velY + (self._float_accelerationY*float_deltaTime)*int_accelerationBust, -self._int_velMax, self._int_velMax)


        int_newVelX = limits(int(self._float_velX), -self._int_velMax, self._int_velMax)
        int_newVelY = limits(int(self._float_velY), -self._int_velMax, self._int_velMax)
        if int_newVelX != self._int_velX or int_newVelY != self._int_velY :
            self._int_velX = int_newVelX
            self._int_velY = int_newVelY
            self.cam.pantilt(self._int_velX, self._int_velY)
            print(f'Enviado comando vel_X : {self._int_velX} | vel_y :{self._int_velY}')
        # ===========================================================================================================================================


        # ZOOM UPDATE =====================================================================================================
        float_accelerationBustZoom = 2
        float_breakingBustZoom = 0.0005
        if self._float_breakingZoom != 0.0: # breaking zoom
            if self._int_velZoom != 0: #has to break 
                int_accelerationSignalZoom = 1 if self._float_velZoom < 0 else -1
                self._float_velZoom = self._float_velZoom + int_accelerationSignalZoom*self._float_breakingZoom*float_breakingBustZoom
            elif self._int_velZoom == 0:
                self._float_breakingZoom = 0.0
        else: #accelerating
            self._float_velZoom = limits(self._float_velZoom + self._float_accelerationZoom*float_deltaTime*float_accelerationBustZoom, -7, 7)

        int_newVelZoom = int(self._float_velZoom)
        if self._int_velZoom != int_newVelZoom:
            self._int_velZoom = limits(int_newVelZoom, -7, 7)
            self.cam.zoom(self._int_velZoom)
            print(f'Enviado comando vel_Zoom : {self._int_velZoom}')


        # =====================================================================================================

        self.__float_lastUpdateTime = float_currentTime

    def load_position(self, x, y, zoom, vel_x, vel_y, vel_max):
        int_x = int(limits(x, -2148, 2148))
        int_y = int(limits(y, -2148, 2148))
        float_zoom = float(limits(zoom, 0.0, 1.0))
        int_velX = abs(int(limits(vel_x*24, -vel_max, vel_max)))
        int_velY = abs(int(limits(vel_y*24, -vel_max, vel_max)))
        self.cam.pantilt(int_velX, int_velY, pan_position=int_x, tilt_position=int_y)
        self.cam.zoom_to(float_zoom)
        print(f'Enviado comando de posição x : {int_velX} | y : {int_velY} | zoom : {float_zoom} | vel_x : {int_velX} | vel_y : {int_velY}')
        pass

    def stop(self):
        self._int_velX=0
        self._int_velY=0
        self._float_velX=0.0
        self._float_velY=0.0
        self._float_accelerationX=0.0
        self._float_accelerationY=0.0
        self._float_breakingAcceleration=0.0 # breaking acceleration when button is released

        self._float_velZoom=0.0
        self._float_accelerationZoom=0.0
        self._float_breakingZoom=0.0
        self._int_velZoom=0 

        self.cam.pantilt(0, 0)
        self.cam.zoom(0)
        print(f'Enviado comando vel_X : {self._int_velX} | vel_y :{self._int_velY}')
        print(f'Enviado comando vel_Zoom : {self._int_velZoom}')



        
    # Getters -------------------------------------------
    @property
    def x(self):
        pos = self.cam.get_pantilt_position()
        self._int_x = pos[0]
        self._int_y = pos[1]
        return self._int_x
    
    @property
    def y(self):
        pos = self.cam.get_pantilt_position()
        self._int_x = pos[0]
        self._int_y = pos[1]
        return self._int_y
    
    @property
    def pos(self) -> list[int,int,int]: 
        pos = self.cam.get_pantilt_position()
        self._int_x = pos[0]
        self._int_y = pos[1]
        float_zoom = self.cam.get_zoom_position()/16384
        return (self._int_x, self._int_y, float_zoom)
    
    @property
    def vel_x(self):
        return self._float_velX

    @property
    def vel_y(self):
        return self._float_velY
    
    @property
    def vel_max(self):
        return self._int_velMax

    @property
    def acceleration_x(self):
        return self._float_accelerationX

    @property
    def acceleration_y(self):
        return self._float_accelerationY
    
    @property
    def breaking(self):
        return self._float_breakingAcceleration

    @property
    def vel_zoom(self):
        return self._float_velZoom
    
    @property
    def acceleration_zoom(self):
        return self._float_accelerationZoom
    
    @property
    def breaking_zoom(self):
        return self._float_breakingZoom


    # Setters -------------------------------------------
    @vel_x.setter
    def vel_x(self, value : float):
        value = limits(value, -24, 24)
        self._float_velX = float(value)
    
    @vel_y.setter
    def vel_y(self, value : float):
        value = limits(value, -24, 24)
        self._float_velY = float(value)

    @vel_max.setter
    def vel_max(self, value):
        value = limits(value, -24, 24)
        self._int_velMax = abs(int(value))

    @acceleration_x.setter
    def acceleration_x(self, value : float):
        # todo : define limits
        self._float_accelerationX = value

    @acceleration_y.setter
    def acceleration_y(self, value : float):
        # todo : define limits
        self._float_accelerationY = value

    @breaking.setter
    def breaking(self, value : float):
        # todo : define limits
        self._float_breakingAcceleration = value
    
    @vel_zoom.setter
    def vel_zoom(self, value : float):
        # todo : define limits
        self._float_velZoom = limits(value*7, -7.0, 7.0)
    
    @acceleration_zoom.setter
    def acceleration_zoom(self, value : float):
        self._float_accelerationZoom = value
    
    @breaking_zoom.setter
    def breaking_zoom(self, value : float):
        self._float_breakingZoom = value

    
    
    