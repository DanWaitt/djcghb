text = """
WEB Desarrollo 445304097621 us-east-1
AyF Desarrollo 543004080678 us-east-1
Amarumayu Productivo 949387832168 us-east-1 *
AJILES Integraciones 590183686173 us-east-1 *
Web AJE 916165595678 us-east-1
Analitica Desarrollo 832257724409 us-east-1
Asia-ERP 942060068409 us-east-1
AJILES Network 058264262466 us-east-1
Feniziam_Outbound 646859577627 us-east-1
Audit 445455402530 us-east-1
AJILES Analitica 992382850463 us-east-1
AJE TI Global Productivo 946989562158 us-east-1
Feniziam_Produccion 657928216603 us-east-1
Asia-Security 073501450314 us-east-1
AJE_Shared_Services 778158354266 us-east-1
Latam ERP Econored 891377326260 us-east-1
Feniziam_Security 263482044980 us-east-1
Asia-Cadena 791127147790 us-east-1
Feniziam Desarrollo 054928539393 us-east-1
Bioamayu Productivo 972045392774 us-east-1
AJILES Desarrollo 975050119475 us-east-1
AJE Main Account 054540046776 us-east-1
AJILES Comercial 851725533058 us-east-1
Feniziam_Test 972415495655 us-east-1
AJILES TI Global 905418143230 us-east-1
Log archive 283006227576 us-east-1
Comercial Desarrollo 819334634599 us-east-1
Feniziam_Inbound 745226216622 us-east-1
Network 381491963897 us-east-1
AJILES ERP 211125648884 us-east-1

WEB Desarrollo 445304097621 us-east-2
AyF Desarrollo 543004080678 us-east-2
Web AJE 916165595678 us-east-2
Analitica Desarrollo 832257724409 us-east-2
Asia-TD-Global 705357548934 us-east-2
Feniziam_Outbound 646859577627 us-east-2
Latam ERP Desarrollo 211125461000 us-east-2
Audit 445455402530 us-east-2
ANALITICA DEPLOY 153291103677 us-east-2
Kissflow Productivo 426460723866 us-east-2
Cadena Produccion 734293319718 us-east-2
AJE TI Global Productivo 946989562158 us-east-2
Feniziam_Produccion 657928216603 us-east-2
Asia-Security 073501450314 us-east-2
AJE_Shared_Services 778158354266 us-east-2
Latam ERP Econored 891377326260 us-east-2
Feniziam_Security 263482044980 us-east-2
Analitica Productivo 399723489351 us-east-2
Feniziam Desarrollo 054928539393 us-east-2
Cadena Desarrollo 233702604775 us-east-2
Comercial Productivo 152109476108 us-east-2
Integ Oracle Productivo 654654223555 us-east-2
Bioamayu Productivo 972045392774 us-east-2
AyF Produccion 096281107371 us-east-2
Analitica_Test 539323487453 us-east-2
AJE Main Account 054540046776 us-east-2
Latam ERP 637423469932 us-east-2
Log archive 283006227576 us-east-2
Africa-ERP 487012554816 us-east-2
Comercial Desarrollo 819334634599 us-east-2
Feniziam_Inbound 745226216622 us-east-2
Network 381491963897 us-east-2
AJILES ERP 211125648884 us-east-2
Cadena Deploy 252958272093 us-east-2
Latam ERP Econored Desarrollo 058264415966 us-east-2

Asia-Desarrollo 112956914731 ap-southeast-1
Amarumayu Productivo 949387832168 ap-southeast-1
AJILES Integraciones 590183686173 ap-southeast-1
Web AJE 916165595678 ap-southeast-1
Analitica Desarrollo 832257724409 ap-southeast-1
Asia-ERP 942060068409 ap-southeast-1
Asia-TD-Global 705357548934 ap-southeast-1
Feniziam_Outbound 646859577627 ap-southeast-1
Audit 445455402530 ap-southeast-1
Asia-Outbound 392322900251 ap-southeast-1
AJILES Analitica 992382850463 ap-southeast-1
Cadena Produccion 734293319718 ap-southeast-1
AJE TI Global Productivo 946989562158 ap-southeast-1
Feniziam_Produccion 657928216603 ap-southeast-1
AJE_Shared_Services 778158354266 ap-southeast-1
Latam ERP Econored 891377326260 ap-southeast-1
Asia-Inbound 585978463622 ap-southeast-1
Asia-Cadena 791127147790 ap-southeast-1
Integ Oracle Productivo 654654223555 ap-southeast-1
Asia-Analitica 304007336319 ap-southeast-1
Bioamayu Productivo 972045392774 ap-southeast-1
AJILES Desarrollo 975050119475 ap-southeast-1
AJE Main Account 054540046776 ap-southeast-1
Latam ERP 637423469932 ap-southeast-1
AJILES Comercial 851725533058 ap-southeast-1
Feniziam_Test 972415495655 ap-southeast-1
AJILES TI Global 905418143230 ap-southeast-1
Comercial Desarrollo 819334634599 ap-southeast-1
Feniziam_Inbound 745226216622 ap-southeast-1
Asia-Comercial 019026144894 ap-southeast-1
"""

lines = text.split("\n")
unique_lines = list(set(lines))
result = "\n".join(sorted(unique_lines))

print(result)