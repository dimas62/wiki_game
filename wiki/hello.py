# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import urllib
from lxml import html, etree 


def hello(request):
	
	#url = "http://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F"
	#page = html.fromstring(urllib.urlopen(url).read())

	#cont = page.xpath("//div[@id='content']")
	t = get_template('index.html')
	#string = html.tostring(cont)
	htmlq = t.render(Context())
	return HttpResponse(htmlq)	