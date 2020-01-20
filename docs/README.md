###### Para criar o site primeiro criamos os seguintes arquivos
- [x] _config.yml
- [x] index.md

###### e a pasta que contém os arquivos que serão incluídos no site pelo index.md
- [x] _includes

###### tem como escrever posts de blog na seguinte pasta
- [x] _posts

> O nome do post tem que seguir o seguinte formato _ano-mes-dia-título.md_
> O post tem o seguinte formato:
>

```
---
title: "Título"
date: data (ano-mes-dia)
---

 Seu Post 

```
---
layout: default
---

{% include nome-do-arquivo-1.md %}

<br>

{% include nome-do-arquivo-2.md %}

<br>

{% include nome-do-arquivo-3.md %}

<br>

{% include nome-do-arquivo-4.md %}

<br>

{% include nome-do-arquivo-5.md %}
```
