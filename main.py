

from bs4 import BeautifulSoup

variable = open("covSummary.html","r")
variable1 = variable.read()
variable2 = BeautifulSoup(variable1,'lxml')
print(variable2.prettify())