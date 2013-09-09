title: Search
subtitle: Columns template
description: Test description
---

{% extends "topbar.j2" %}

{% block container %}

<h2> Search </h2>

{% raw %}
<?php include_once("searcher.php"); ?>
{% endraw %}

{% endblock container %}
