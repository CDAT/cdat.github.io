---
title: Display
subtitle: Columns template
description: Test description
---

{% extends "php.j2" %}

{% block post_content_php %}
<?php include_once("displayer.php"); ?>
{% endblock post_content_php %}
