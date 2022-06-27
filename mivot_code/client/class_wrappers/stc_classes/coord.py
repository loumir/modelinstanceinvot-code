'''
Created on 20 Jan 2022

@author: laurentmichel
'''
from ..component_builder import ComponentBuilder
from .components import Quantity

class Coord(object):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        self.dmtype = None
        self.coordSys = None
        self._set_coord_sys(model_view)
        
        self.label = f"{self.__class__} {self.coordSys.label}"
       
    def _set_coord_sys(self, model_view): 
        for ele in model_view.xpath('.//INSTANCE[@dmrole="coords:Coordinate.coordSys"]'):
            self.coordSys = ComponentBuilder.get_coordsys(ele)

class PhysicalCoordinate(Coord):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        super().__init__(model_view)
        self.cval = None
        self.dmtype = "PhysicalCoordinate"

        
        for ele in model_view.xpath('.//INSTANCE[@dmrole="coords:PhysicalCoordinate.cval"]'):
            self.cval = Quantity(ele)
            break
        
        self.label = f"[{self.cval.value} {self.cval.unit} {self.coordSys.label}]"

    def __repr__(self):
        return self.label

class TimeStamp(Coord):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        super().__init__(model_view)
        pass
 
    def __repr__(self):
        return self.label
    
class ISOTime(Coord):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        super().__init__(model_view)
        self.datetime = None
        self.dmtype = "ISOTime"
        
        for ele in model_view.xpath('.//ATTRIBUTE[@dmrole="coords:ISOTime.date"]'):
            self.datetime = ele.get("value")
            break
        
    def __repr__(self):
        return self.label
        
class Point(Coord):
    '''
    classdocs
    '''


    def __init__(self, model_view):
        '''
        Constructor
        '''
        super().__init__(model_view)
        pass
    
    @staticmethod 
    def get_point(model_view):
        dmtype = model_view.get("dmtype")
        if dmtype == "coords:LonLatPoint":
            return LonLatPoint(model_view)
        else:
            raise Exception(f"Point type {dmtype} not supported yet")

    
class LonLatPoint(Point):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        super().__init__(model_view)
        self.lon = None
        self.lat = None
        self.dist = None
        self.dmtype = "LonLatPoint"
        
        for ele in model_view.xpath('.//INSTANCE[@dmrole="coords:LonLatPoint.lon"]'):
            self.lon = Quantity(ele)

        for ele in model_view.xpath('.//INSTANCE[@dmrole="coords:LonLatPoint.lat"]'):
            self.lat = Quantity(ele)

        self.label = f"[{self.lon.value} {self.lat.value} {self.lat.unit} {self.coordSys.label}]"
        
    def __repr__(self):
        return self.label

        