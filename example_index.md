---
title: Examples Index
layout: default
---

[Back to the Gallery](/gallery.html)

<div class="row">
<div class="col-md-3">
<h4>Boxfill Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "boxfill" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul>
</div>

<div class="col-md-3"><h4>Isofill Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "isofill" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>

<div class="col-md-3"><h4>Isoline Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "isoline" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>


<div class="col-md-3"><h4>Meshfill Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "meshfill" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>

</div>

<div class="row">

<div class="col-md-3"><h4>Scatter Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "scatter" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>


<div class="col-md-3"><h4>Vector Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "vector" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>


<div class="col-md-3"><h4>XvsY Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "xvsy" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>

<div class="col-md-3"><h4>XYvsY Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "xyvsy" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>
</div>
<div class="row">
<div class="col-md-3"><h4>YXvsX Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "yxvsx" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>

<div class="col-md-3"><h4>1D Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "1d" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>

<div class="col-md-3"><h4>3D Scalar Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "3d_scalar" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>


<div class="col-md-3"><h4>3D Vector Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "3d_vector" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>
</div>
<!--
<div class="col-md-3"><h4>Taylor Diagram Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "taylordiagram" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>

<div class="col-md-3"><h4>3D Dual Scalar Examples</h4>

<ul>
{% for ex in site.examples %}
    {% for tag in ex.tags %}
        {% if tag == "3d_dual_scalar" %}
        <li><a href="{{ex.url}}">{{ex.title}}</a></li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul></div>
-->