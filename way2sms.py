import requests 
import json 
import re 
from flask import Flask, session, url_for, render_template, request, redirect, flash, abort

print __name__

app = Flask(__name__)

print app

URL = 'https://www.way2sms.com/api/v1/sendCampaign'
# get request 
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage): 
  req_params = {
    'apikey':apiKey,
    'secret':secretKey,
    'usetype':useType,
    'phone': phoneNo,
    'message':textMessage,
    'senderid':senderId
  }
  app.logger.info("reqUrl: %s" % reqUrl)
  app.logger.info("req_params: %s" % req_params)
  return requests.post(reqUrl, req_params)

def alertDailog(msg, redirect):
  if not redirect:
    redirect = "/"
  return "<script>window.alert(\"{msg}\");window.location.href=\"{url}\";</script>".format(msg=msg, url=redirect)

def form_ui():
  doc = '<form action="/msg" method="POST"><table><tr><td>Mobile No:</td><td> <input type="number" name="mobileNo" autofocus></td></tr><tr><td>Msg:</td><td> <input type="text" name="textMsg"></td></tr><tr><td></td><td> <input type="submit" value="Send"></td></tr></table></form>'
  return doc

@app.route('/msg', methods=['POST'])
def msg():
  responseMsg = "Did not send message."
  mobileNo = request.form['mobileNo']
  textMsg = request.form['textMsg']
  if not mobileNo:
    return alertDailog("Mobile is not found.", "/")
  elif re.match("([0-9]{10})", mobileNo) is None:
    return alertDailog("It's not mobile.", "/")
  elif not textMsg:
    return alertDailog("Msg text is not found.", "/")
    
  response = {"remaining-sms":16} #{"code":"200 OK","total-messages-sent":1,"req-type":"post","remaining-sms":16,"message":"Campaign sent successfully.","usetype":"stage","balacne":"0","status":"success"}

  try:
    # get response 
    # prod/stage
    # response = sendPostRequest(URL, '11UCB7XUZ2Y1SLKOK6M1NP2U020FB1T4', '2NE0HYWB7VXHKG75', 'stage', mobileNo, '1500', textMsg ) 
    # response = {"code":"200 OK","total-messages-sent":1,"req-type":"post","remaining-sms":16,"message":"Campaign sent successfully.","usetype":"stage","balacne":"0","status":"success"} 
    """ 
       Note:- 
       you must provide apikey, secretkey, usetype, mobile, senderid and message values 
       and then requst to api 
    """ 
    #{"code":"200 OK","total-messages-sent":1,"req-type":"post","remaining-sms":16,"message":"Campaign sent successfully.","usetype":"stage","balacne":"0","status":"success"}
    # print response if you want 
    app.logger.info("response: %s" % response)
    if response and response["remaining-sms"]:
      responseMsg="Message will be sent remaining %d seconds." % response["remaining-sms"]
  except Exception as e:
    app.logger.info("response: %s" % e)

  return alertDailog(responseMsg, "/")


@app.route('/')
def msg_form():
  return form_ui()


if __name__=="__main__":
  app.run(debug=True,host="127.0.0.1",port=8080)
  pass