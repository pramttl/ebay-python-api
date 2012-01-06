from configparser import ConfigParser
import httplib2
from urllib.parse import urlencode
from xml.dom.minidom import parse, parseString
import struct

def main():
  print(getCategories())

def addListing(options):
  #xml = buildxml(options)
  #return etree.tostring(xml, pretty_print=True)
  pass


def getCategories():
  pass



class Request:
  def __init__(self):
    config = ConfigParser()
    config.read('config.ini')
    self.app_id = config.get('keys', 'app_name')
    self.dev_name config.get('keys', 'dev_name')
    self.cert_name config.get('keys', 'cert_name')
    self.site_id = config.get('call', 'siteid')
    self.version = config.get('call', 'compatibility_level')
    self.endpoint = config.get('endpoints', 'shopping')

    self.auth_token = config.get('auth', 'token')

  def construct_xml(self, request = {}):
    request.update({
      'type': {'name': 'GeteBayOfficialTimeRequest', 'content': 'xmlns="urn:ebay:apis:eBLBaseComponents"'},
      'RequesterCredentials': {'eBayAuthToken': self.auth_token},
      'Version': '747'
    })
    defaultXml = '<?xml version="1.0" encoding="utf-8"?><'+request['type']['name']+' '+request['type']['content']+'><RequesterCredentials><eBayAuthToken>'+request['RequesterCredentials']['eBayAuthToken']+'</eBayAuthToken></RequesterCredentials><Version>'+request['Version']+'</Version></'+request['type']['name']+'>'
    dom = parseString(defaultXml)
     
    return dom

  def construct_header(self, header):
    defaultHeader = {
      'X-EBAY-API-COMPATIBILITY-LEVEL': self.version,
      'X-EBAY-API-DEV-NAME': 
        
    }

  def trading(self, params = {}, headers={}, method="POST"):
    """
      sends a request to the ebay trading api via xml
    """
    data = dict(appid = self.app_id, siteid = self.site_id, version = self.version)
    data.update(params)
    headers = dict()
    headers.update(headers)
    h = httplib2.Http(".cache")
    if data and method=="GET":
      url = endpoint + '?' + urlencode(data)
    elif data and method=="POST":
      url = endpoint
      body = urlencode(data)


    resp, content = h.request(url, method=method, headers=headers, body=body)
    print (resp)
    print (content)
    print (url)


if __name__ == '__main__':
  request = Request()
  #print(dir(request.construct_xml({"määh": "muuh"})))
  print(request.construct_xml({"määh": "muuh"}).toxml())

  main()
