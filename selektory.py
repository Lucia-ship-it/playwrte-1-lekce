#textove selektory = vnutorny text - dvoje uvodzovky, v produkcnych textoch by sa nemali vyskytovat
"text = 'Prehled IT kurzu'"


# CSS selektory - zo stranky
"body >div.intercom-light......"

# typovy selektor
"div"
"h1"
"input"



# atributy / selector tridy, ked ich je viac za sebou su oddelene len medzerou
#class
".container"

# selector id - na stranke len 1x
"#main-header"

#ostatne atributy
"[type='password']"
"[name='password']"

<h1 class="nadpis-2" type="nadpis">Nadpis 2</h1>
z tohoto kodu selektory aby sme mohli vybrat h1

"h1"
".nadpis-2"
"[type='nadpis']"

# spojenie viac vlastnosti, pise sa za seba bez medzier
"h1.nadpis-2[type='nadpis']"

# druhy typ s medzerou vyuziva strukturu
"div h1" # v div hlada h1

".container-2 h1"
"body .conteiner-2 h1"

# a oba postupy sa daju kombonovat dohromdy
"body div.container-2 h1.nadpis-2"
<body>
  <div class="container">
    <h1><span class="nadpis">Nadpis 1</span></h1>

"body div.container h1.nadpis[type='nadpis']"


#XPath
