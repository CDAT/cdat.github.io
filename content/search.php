---
title: Search
subtitle: Columns template
description: Test description
---

{% extends "php.j2" %}

{% block container %}
<h2> Search </h2>
{% endblock container %}

{% block post_content_php %}
<?php include_once("searcher.php"); ?>
{% endblock post_content_php %}
