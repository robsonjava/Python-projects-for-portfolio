import camelcase

txt = "robson bento"

str = camelcase.CamelCase().hump(txt)

print(str)