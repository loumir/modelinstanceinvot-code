'''
Created on 30 Jan 2022

@author: laurentmichel
'''

class PhotCal(object):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        self.identifier = None
        self.zeroPoint = None
        self.photometryFilter = None
        self.magnitudeSystem = None
        
        for ele in model_view.xpath('.//INSTANCE[@dmrole="photdm:PhotCal.zeroPoint"]'):
            self.zeroPoint = ZeroPoint.get_zero_point(ele)
            break
        
        for ele in model_view.xpath('.//INSTANCE[@dmrole="photdm:PhotCal.photometryFilter"]'):
            self.photometryFilter = PhotometryFilter(ele)
            break
        
        for ele in model_view.xpath('.//INSTANCE[@dmrole="photdm:PhotCal.magnitudeSystem"]'):
            self.magnitudeSystem = MagnitudeSystem(ele)
            break
            
        for ele in model_view.xpath('.//ATTRIBUTE[@dmrole="photdm:PhotCal.identifier"]'):
            self.identifier = ele.get("value")
            break
        
    def __repr__(self):
        return f"{self.identifier}\n"\
            f"   filter {self.photometryFilter}"
       
class MagnitudeSystem(object):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        self.type = None
        self.referencesSpectrum = None

    def __repr__(self):
        return f"ucd: {self.ucd} coords: {self.coord} error: {self.error}"
    
    
class PhotometryFilter(object):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        self.fpsidentifier = None
        self.identifier = None
        self.name = None
        self.description = None
        self.bandname = None
        self.dateValidityFrom = None
        self.dateValidityTo = None
        
        self.photometricFilter = None
        self.spectralLocation = None
        self.bandwidth = None
        self.transmissionCurve = None
        
        

        for ele in model_view.xpath('.//ATTRIBUTE[@dmrole="photdm:PhotometryFilter.fpsidentifier"]'):
            self.fpsidentifier = ele.get("value")
            break
        for ele in model_view.xpath('.//ATTRIBUTE[@dmrole="photdm:PhotometryFilter.identifier"]'):
            self.identifier = ele.get("value")
            break
        for ele in model_view.xpath('.//ATTRIBUTE[@dmrole="photdm:PhotometryFilter.name"]'):
            self.name = ele.get("value")
            break
        for ele in model_view.xpath('.//ATTRIBUTE[@dmrole="photdm:PhotometryFilter.description"]'):
            self.description = ele.get("value")
            break
        for ele in model_view.xpath('.//ATTRIBUTE[@dmrole="photdm:PhotometryFilter.bandname"]'):
            self.bandname = ele.get("value")
            break
        for ele in model_view.xpath('.//ATTRIBUTE[@dmrole="photdm:PhotometryFilter.dateValidityFrom"]'):
            self.dateValidityFrom = ele.get("value")
            break
        for ele in model_view.xpath('.//ATTRIBUTE[@dmrole="photdm:PhotometryFilter.dateValidityTo"]'):
            self.dateValidityTo = ele.get("value")
            break

    def __repr__(self):
        return f"{self.fpsidentifier}/{self.identifier}/{self.name}/{self.bandname}  {self.description} valid from {self.dateValidityFrom} to {self.dateValidityTo}"
    

class TransmissionCurve(object):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        self.transmissionPoint = []
        self.access = None
        
class Access(object):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        self.reference = None
        self.size = None
        self.format = None
        
class TransmissionPoint(object):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        self.ucd = None
        self.unit = None
        self.transmissionValue = None
        self.spectralValue = None
        self.spectralValueError = None
   
class ZeroPoint(object):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        self.type = None
        self.referencesMagnitudeValue = None
        self.referencesMagnitudeError = None

    def __repr__(self):
        return f"ucd: {self.ucd} coords: {self.coord} error: {self.error}"
    
class PogsonZeroPoint(ZeroPoint):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        ZeroPoint.__init__(self, model_view)

    def __repr__(self):
        return f"ucd: {self.ucd} coords: {self.coord} error: {self.error}"
    
class LinearFluxZeroPoint(ZeroPoint):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        ZeroPoint.__init__(self, model_view)

    def __repr__(self):
        return f"ucd: {self.ucd} coords: {self.coord} error: {self.error}"
    
class AsinhZeroPoint(ZeroPoint):
    '''
    classdocs
    '''
    def __init__(self, model_view):
        '''
        Constructor
        '''
        ZeroPoint.__init__(self, model_view)
        self.softeningParameter = None

    def __repr__(self):
        return f"ucd: {self.ucd} coords: {self.coord} error: {self.error}"
    
       




