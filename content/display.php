title: Display
subtitle: Columns template
description: Test description
---

{% extends "topbar.j2" %}

{% block container %}

{% raw %}
<?php include_once("displayer.php"); ?>
{% endraw %}

{% endblock container %}
