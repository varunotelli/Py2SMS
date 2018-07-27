# Py2SMS
Python3 code to send SMS with Way2Sms

Send upto 100 free [SMS](http://www.way2sms.com/content/index.html) within 10 seconds daily yo any phone number in India.

[Way2Sms](http://www.way2sms.com/content/index.html) provides free SMS service upto **10** messages daily with message length upto **139**. 

### Prerequisites
* Install Python3.x from [here.](https://www.python.org/)
* Create an account in [Way2SMS](www.way2sms.com/)
* Install py2sms using `pip install py2sms`

### How to use Py2SMS

```python
import py2sms
```
-  Sending message

  ```python
s=py2sms.send(username,password,number,message)
  ```
* If message was sent successfully, py2sms.send() will return True, else False

# Disclaimer
This code was inspired by [http://home.iitk.ac.in/~saiwal/productivity/send-sms-way2sms-python/](http://home.iitk.ac.in/~saiwal/productivity/send-sms-way2sms-python/)
