#to check Python packages, go to CMD or terminal, type: "pip --version" to check the version or "pip list" to check the packages
#type import camelcase (for example), execute the code, go to CMD and type "pip install camelcase". It will install it

import camelcase


c = camelcase.CamelCase()
print(c.hump("hello world"))