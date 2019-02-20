 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import mechanize as mec
maliciousRequest = mec.Browser()
formName = 'waf'
maliciousRequest.open("http://check.cyberpersons.com/crossSiteCheck.html")
maliciousRequest.select_form(formName)

input type="text" name="data">

crossSiteScriptingPayLoad = "<svg><script>alert&grave;1&grave;<p>"

maliciousRequest.form['data'] = crossSiteScriptingPayLoad

maliciousRequest.submit()
response =  maliciousRequest.response().read()

print response

if response.find('WebKnight') >= 0:
       print "Firewall detected: WebKnight"
elif response.find('Mod_Security') >= 0:
      print "Firewall detected: Mod Security"
elif response.find('Mod_Security') >= 0:
      print "Firewall detected: Mod Security"
elif response.find('dotDefender') >= 0:
      print "Firewall detected: Dot Defender"
else:
      print "No Firewall Present