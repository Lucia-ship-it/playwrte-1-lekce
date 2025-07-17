Máme tento html kód:

```html
<body>
  <div class="container">
    <h1><span class="nadpis">Nadpis 1</span></h1>
  </div>
  <div class="container-2">
    <h1 class="nadpis-2" type="nadpis">Nadpis 2</h1>
  </div>
</body>
```

# 1. úkol:

_Jak bychom pojmenovali 2. nadpis v této ukázce (slovně):_
Např:

- h1 s atributem class s hodnotou "nadpis-2"
- element h1 v elementu se třídou "container-2"

# 2. úkol

_Napiš textový lokátor pro 2. nadpis v této ukázce:_

- `locator = page.locator("text='Nadpis 2'")`

# 3. úkol

_Napiš 2 různé CSS lokátory pro 2. nadpis v této ukázce:_

- `locator = page.locator(".nadpis-2")`
- `locator = page.locator("#nadpis")`
- `locator = page.locator("container-2 > h1")`

# 4. úkol

_Napiš lokátor pro 2. nadpis v ukázce pomocí funkce `nth()`_

- `locator = page.locator("h1").nth(1)`
