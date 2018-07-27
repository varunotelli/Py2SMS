import urllib.request, urllib.error, urllib.parse
import http.cookiejar

def send(username,password,number,message=''):
	
	message = "+".join(message.split(' '))

	
	url = 'http://www.way2sms.com/re-login'
	data = 'mobileNo='+username+'&password='+password+'&CatType'
	 
	#For Cookies:
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	 
	# Adding Header detail:
	opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
	 
	try:
	    socket = opener.open(url, data.encode('utf-8'))
	except :
	    return False
	    
	 
	 
	session_id = str(cj).split('~')[1].split(' ')[0]
	smsurl = 'http://www.way2sms.com/smstoss'
	data = 'ssaction=ss&Token='+session_id+'&toMobile='+number+'&message='+message
	opener.addheaders = [('Referer', 'http://www.way2sms.com/send-sms'+session_id)]
	 
	try:
	    page = opener.open(smsurl,data.encode('utf-8'))
	except:
	    return False
	
	return True

