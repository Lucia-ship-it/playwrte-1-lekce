# 1. úkol

Máme tento kus html:

```html
<div class="kontejner">
  Tady je nadpis.
  <img id="obrazek" type="big" />
</div>
```

Zodpověz tyto otázky:

_Kolik html elementů v daném kódu figuruje?_
2 - jeden z nich je `<div>` a druhý je `<img>`.

_Který z elementů je rodič a který je potomek?_
`<div>` obalujem element `<img>`, a tak je rodičem img, zatímco `<img>` je potomkem elementu `<div>`

_Ke kterému elementu patří text "Tady je napdis."?_
Tento text patří k elementu `<div>`, protože se nachází uvnitř tohoto elemntu.

_Může mít tag `<img>` nějaký další element v sobě?_
Aktuálně ne - je tvořen pouze jedním tagem (nemá otevírací a uzavírací tag, mezi které by se mohli vložit další element)

_Může mít tag `<div>` nějaký další element v sobě?_
Ano může - má otevírací a zavírací tag, a tak do něj můžeme vkládat elementy. Zároveň dovnitř elementu můžeme vložit neomezeně mnoho dalších elementů.

_Kolik atributů má `<h1>`?_
2

_Vyjmenuj atributy elementu `<div>` a jejich hodnoty._
Element `<div>` má jeden atribut, který se jemnuje "class" (nebo česky "třída") a jeho hodnota je "kontejner".
