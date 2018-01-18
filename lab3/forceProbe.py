from H3DInterface import *
from math import sqrt

class CalcForce(TypedField(SFVec3f,(SFVec3f ,MFBool))):
    sphereCenter = Vec3f(0,0,0)
    sphereRadii = 0.08
    
    def dist(self, wandPosX, wandPosY, wandPosZ):
        return sqrt(pow(wandPosX,2) + pow(wandPosY,2) + pow(wandPosZ,2))
    
    def update(self, event):
        #k in N/m constant of hookes law
        k = 1400
        x = 0.0

        #add virtual probe
        xPos = event.getValue().x * 0.98
        yPos = event.getValue().y * 0.98
        zPos = event.getValue().z * 0.98
        
        
        distance = self.dist(xPos,yPos,zPos)
        
        if distance <= self.sphereRadii:
            x = self.sphereRadii - distance
            #check for zero division error
            if distance == 0:
                return Vec3f(0,0,0)
            xForce = (xPos/distance) * x * k
            yForce = (yPos/distance) * x * k
            zForce = (zPos/distance) * x * k
            return Vec3f(xForce,yForce,zForce)
        else:
            return Vec3f(0,0,0)
                
calcForce = CalcForce() 