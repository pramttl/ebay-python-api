from configparser import ConfigParser
import httplib2
from urllib.parse import urlencode
from xml.dom.minidom import parse, parseString
from lxml import etree
import struct

def main():
  request = EbayRequest()
  print(request.AddItem())

class EbayRequest:
  """
    Class assists in making requests to the ebay trading api
    Workhore function is Request.trading
  """
  def __init__(self):
    config = ConfigParser()
    config.read('config.ini')
    self.app_id = config.get('keys', 'app_name')
    self.dev_name = config.get('keys', 'dev_name')
    self.cert_name = config.get('keys', 'cert_name')
    self.site_id = config.get('call', 'siteid')
    self.version = config.get('call', 'compatibility_level')
    self.endpoint = config.get('endpoints', 'trading')

    self.auth_token = config.get('auth', 'token')

  def dict2xml(self, data):
    xml = ""
    for key in data:
      if isinstance(data[key], dict):
        xml = xml + '<' + key + '>' + self.dict2xml(data[key]) + '</' + key.split()[0] + '>'
      else:
        if data[key]: # if data[key] is empty we assume a self closing tag
          xml = xml + '<' + key + '>' + data[key] + '</' + key + '>'
        else:
          xml = xml + '<' + key.split()[0] + ' />'
    return xml


    return xml
  def construct_xml(self, request = 'GeteBayOfficialTimeRequest', params = None):
    dom = etree.Element(request, xmlns='urn:ebay:apis:eBLBaseComponents')

    if isinstance(params, str):  # check if params is given as a xml string
      params = etree.XML(params)
    if params: 
      if params.__class__ == '<class \'lxml.etree._Element\'>':
        if not params.find('.//RequesterCredentials'):
          requesterCredentials = etree.XML('<RequesterCredentials><eBayAuthToken>' + self.auth_token + '</eBayAuthToken></RequesterCredentials>')
          version = etree.XML('<Version>' + self.version + '</Version>')
          dom.append(requesterCredentials)
          dom.append(version)
        dom.append(params)

    return dom

  def construct_header(self, header, request):
    defaultHeader = {
      'X-EBAY-API-COMPATIBILITY-LEVEL': self.version,
      'X-EBAY-API-DEV-NAME': self.dev_name,
      'X-EBAY-API-APP-NAME': self.app_id,
      'X-EBAY-API-CERT-NAME': self.cert_name,
      'X-EBAY-API-CALL-NAME': request,
      'X-EBAY-API-SITEID': self.site_id,
      'X-EBAY-API-DETAIL-LEVEL': '0',
      'Content-Type': 'text/xml',
      'X-EBAY-API-RESPONSE-ENCODING': 'JSON'
    }
    defaultHeader.update(header)
    return defaultHeader

  def trading(self, request = "GeteBayOfficialTimeRequest", params = {}, headers = {}, method = "POST"):
    """
      sends a request to the ebay trading api via xml 
    """
    data = self.construct_xml(request, params)
    requestName = request.replace('Request', '') 
    headers = self.construct_header(headers, requestName) 
    h = httplib2.Http(".cache")

    #if data and method=="GET":
    #  url = self.endpoint + '?' + urlencode(data)
    #elif data and method=="POST":
    url = self.endpoint
    body = data

    print('requestName:', requestName, '\n')
    print (url, '\n')
    print ('headers:\n', headers, '\n')
    print ('DOM:\n', '<?xml version="1.0" encoding="utf-8"?>' + etree.tostring(body).decode('UTF-8'), '\n')
    resp, content = h.request(url, method=method, headers=headers, body='<?xml version="1.0" encoding="utf-8"?>'+etree.tostring(body).decode('UTF-8'))
    #print (resp
    #print (content)
    #print (url)
    #print (header)
    return resp, content


  def GeteBayOfficialTime(self):  # gets official time from ebay server (using trading api endpoint)
    request = EbayRequest()
    return request.trading()

  def AddFixedPriceItem():
    pass

  def AddItem(self, item = {}):  # item is a dom object or a dictionary

    if item:
      return self.trading(request = 'AddItemRequest', params = item)
    else:
      return None

  def AddItems():
    pass
  def AddToItemDescription():
    pass
  def CompleteSale():
    pass
  def ConfirmIdentity():
    pass
  def DeleteMyMessages():
    pass
  def EndFixedPriceItem():
    pass
  def EndItem():
    pass
  def EndItems():
    pass
  def FetchToken():
    pass
  def GetAccount():
    pass
  def GetAdFormatLeads():
    pass
  def GetAllBidders():
    pass
  def GetApiAccessRules():
    pass
  def GetFeedback():
    pass
  def GetItem():
    pass
  def GetItemRecommendations():
    pass
  def GetItemsAwaitingFeedback():
    pass
  def GetItemShipping():
    pass
  def GetItemTransactions():
    pass
  def GetMemberMessages():
    pass
  def GetMyeBaySelling():
    pass
  def GetOrders():
    pass
  def GetOrderTransactions():
    pass
  def GetPopularKeywords():
    pass
  def GetSellerDashboard():
    pass
  def GetSellerEvents():
    pass
  def GetSellerList():
    pass
  def GetSellerPayments():
    pass
  def GetSellerTransactions():
    pass
  def GetSessionID():
    pass
  def GetStore():
    pass
  def GetTokenStatus():
    pass
  def GetUser():
    pass
  def GetUserContactDetails():
    pass
  def GetUserDisputes():
    pass
  def RelistFixedPriceItem():
    pass
  def RelistItem():
    pass
  def RespondToFeedback():
    pass
  def RespondToWantItNowPost():
    pass
  def ReviseCheckoutStatus():
    pass
  def ReviseFixedPriceItem():
    pass
  def ReviseInventoryStatus():
    pass
  def ReviseItem():
    pass
  def RevokeToken():
    pass
  def SendInvoice():
    pass
  def SetPromotionalSale():
    pass
  def SetPromotionalSaleListings():
    pass
  def SetShippingDiscountProfiles():
    pass
  def SetStore():
    pass
  def SetStoreCategories():
    pass
  def SetTaxTable():
    pass
  def ValidateTestUserRegistration():
    pass
  def VerifyAddFixedPriceItem():
    pass
  def VerifyAddItem():
    pass
  def VerifyAddSecondChanceItem():
    pass
  def VerifyRelistItem():
    pass


if __name__ == '__main__':
  main()
