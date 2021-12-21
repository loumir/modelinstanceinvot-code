'''
Created on 21 Dec 2021

@author: laurentmichel
'''
import lxml
import xmltodict
from numpy import float64

from client.xml_interpreter.json_block_extractor import JsonBlockExtractor
class ToJsonConverter(object):
    '''
    classdocs
    '''


    def __init__(self, xml_instance):
        '''
        Constructor
        :param xml_instance: XML view of the instance
        :type  xml_instance: etree
        '''
        self.xml_instance = xml_instance
        self.json_instance = None
        
    def _translate_xml(self):
        xmv = lxml.etree.tostring(self.xml_instance)
        tmp_json_block = xmltodict.parse(xmv) 
        tmp_json_block_tmpl = tmp_json_block["TEMPLATES"]
        self.json_instance = {}
        self.json_instance[tmp_json_block_tmpl["@tableref"]] = []
        tbl = self.json_instance[tmp_json_block_tmpl["@tableref"]]
        for key, value in tmp_json_block_tmpl.items():
            if key.startswith("@") is True:
                continue
            tbl.append(value)
    
    def _revert_collections(self):
        revert_coll = JsonBlockExtractor.search_array_container(self.json_instance, "COLLECTION")
        for item in revert_coll:
            item["host"][item["content"]["@dmrole"]]  = [] 
            coll_mapping = item["host"][item["content"]["@dmrole"]]
            for key, value in item["content"].items():
                if key != '@dmrole':
                    if isinstance(value, list):
                        for li in value:
                            coll_mapping.append(li)
                    
            item["host"].pop(item["key"])
            
    def _revert_attributes(self):
        attr_list = JsonBlockExtractor.search_object_container(self.json_instance, "ATTRIBUTE")
        for attr in attr_list:
            content = attr["content"]
            role = content["@dmrole"]
            host = attr["host"]
            host[role] = content
            host[role].pop("@dmrole")
            host.pop(attr["key"])
            self._restore_attribute_type(content)
            # Set role=value can be disabled for debug
            host[role] = content["@value"]
    
    def _restore_attribute_type(self, attr):

        atype = attr["@dmtype"]
        avalue = attr["@value"]
        if atype == "ivoa:boolean":
            attr["@value"] = bool(avalue)
        elif atype == "ivoa:integer":
            attr["@value"] = int(avalue)
        elif atype == "ivoa:RealQuantity" or atype == "ivoa:real":
            attr["@value"] = float64(avalue)
            
    def _revert_instances(self):
        attr_list = JsonBlockExtractor.search_object_container(self.json_instance, "INSTANCE")
        for attr in attr_list:
            content = attr["content"]
            host = attr["host"]
            if isinstance(content, dict):
                role = content["@dmrole"]
                host[role] = content
                host[role].pop("@dmrole")
            else:
                for item in content:
                    host[item["@dmrole"]] = item
                    item.pop("@dmrole")

            host.pop(attr["key"])

    
    def get_json_instance(self):
        self._translate_xml()
        self._revert_collections()
        self._revert_attributes()
        self._revert_instances()
        # just take the content of the key matching the table name
        for _, value in self.json_instance.items():
            return value
        return self.json_instance

