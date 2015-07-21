---
title: VCS Chapter 6
layout: docs
manual: vcs
index: 6
---






##  CHAPTER 6 VCS Primary Objects

In VCS, primary objects define what will be displayed on the VCS Canvas. This
section defines two of the three primary objects and how to modify them
dynamically in the system: graphics methods, which specifies the display
technique; and the picture template, which determines the appearance of each
segment of the display.

**Note**, to see the list of object attributes, use the list() function. For
example:

``` python
import vcs

a=vcs.init()

box=a.createboxfill(`new')
box.list() # This call will list the boxfill attributes and their values

isof=a.createisofill(`new')
isof.list() # This call will list the isofill attributes and their values

tpl=a.createtemplate(`new')
tpl.list() # This call will list the template attributes and their values
```


<table class="table">
    <tr>
      <th rowspan="1" colspan="1">
        Attributes (or Members)
      </th>

      <th rowspan="1" colspan="1">
        Expected Type(s)
      </th>
    </tr>

    <tr>
      <th><a name="boxfill"></a>Object: boxfill</th>

      <th>(graphics method class name is Gfb)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>xaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>yaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>level_1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>level_2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>color_1</code></td>

      <td>IntType: (Range: 0 to 255)</td>
    </tr>

    <tr>
      <td><code>color_2</code></td>

      <td>IntType: (Range: 0 to 255)</td>
    </tr>

    <tr>
      <td><code>legend_type</code></td>

      <td>Either: 'VCS', 'Pts', 'List'</td>
    </tr>

    <tr>
      <td><code>legend</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>ext_1</code></td>

      <td>Either: 'n', 'y'</td>
    </tr>

    <tr>
      <td><code>ext_2</code></td>

      <td>Either: 'n', 'y'</td>
    </tr>

    <tr>
      <td><code>missing</code></td>

      <td>IntType: (Range: 0 to 255)</td>
    </tr>

    <tr>
      <th><a name="continents"></a>Object: continents</td>

      <th>(graphics method
      class name is Gcon)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject or (Either: 'solid','dash','dot',</td>
    </tr>

    <tr>
      <td><code>linecolor</code></td>

      <td>'dash-dot','long-dash', 0,1,2,3,4)</td>
    </tr>

    <tr>
      <td><code>type</code></td>

      <td>IntType: (Range 0 to 255) IntType: (Range 0 to 11)</td>
    </tr>

    <tr>
      <th><a name="isofill"></a>Object: isofill</td>

      <th>(graphics method
      class name is Gfi)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>xaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>yaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>missing</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>ext_1</code></td>

      <td>Either: 'n', 'y'</td>
    </tr>

    <tr>
      <td><code>ext_2</code></td>

      <td>Either: 'n', 'y'</td>
    </tr>

    <tr>
      <td><code>fillareaindices</code></td>

      <td>FillareaObject, or (Either: ListType, or TupleType [Values range 1 to 20])</td>
    </tr>

    <tr>
      <td><code>fillareastyle</code></td>

      <td>Either: 'solid', 'hatch', 'pattern'</td>
    </tr>

    <tr>
      <td><code>fillareacolors</code></td>

      <td>ListType, or TupleType (Index values range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>levels</code></td>

      <td>ListType, TupleType (Values are either integers, floats)</td>
    </tr>

    <tr>
      <th><a name="isoline"></a>Object: isoline</td>

      <th>(graphics method
      class name is Gi)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>xaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>yaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>label</code></td>

      <td>Either: 'n', 'y', 0, 1</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
      2, 3, 4)</td>
    </tr>

    <tr>
      <td><code>linecolors</code></td>

      <td>ListType, TupleType (Values range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>text</code></td>

      <td>TextcombinedObject, TextOrientationObject, TexttableObject, or (Either:
      ListType, TupleType, IntType [Values range 1 to 9])</td>
    </tr>

    <tr>
      <td><code>textcolors</code></td>

      <td>ListType, TupleType (Values range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>level</code></td>

      <td>ListType, TupleType, IntType, FloatType</td>
    </tr>

    <tr>
      <th><a name="outfill"></a>Object: outfill</td>

      <th>(graphics method
      class name is Gfo)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>xaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>yaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>fillareastyle</code></td>

      <td>FillareaObject or (Either: 'solid', 'hatch', 'pattern', 0, 1, 2, 3)</td>
    </tr>

    <tr>
      <td><code>fillareaindex</code></td>

      <td>IntType: (Range 0 to 20)</td>
    </tr>

    <tr>
      <td><code>fillareacolor</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>outfill</code></td>

      <td>ListType, TupleType, IntType, FloatType (must be less than 10 values)</td>
    </tr>

    <tr>
      <th><a name="outline"></a>Object: outline</td>

      <th>(graphics method
      class name is Go)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>xaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>yaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
      2, 3, 4)</td>
    </tr>

    <tr>
      <td><code>linecolor</code></td>

      <td>ListType, TupleType (Values range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>outline</code></td>

      <td>ListType, TupleType, IntType, FloatType (must be less than 10 values)</td>
    </tr>

    <tr>
      <th><a name="scatter"></a>Object: scatter</td>

      <th>(graphics method
      class name is GSp)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>xaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>yaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>marker</code></td>

      <td>MarkerObject or (Either: 'dot', 'plus', 'star', 'circle', 'cross', 'diamond',
      'triangle_up', 'triangle_down', 'triangle_left', 'triangle_right', 'square',
      'diamond_fill', 'triangle_up_fill', 'triangle_down_fill', 'triangle_left_fill',
      'triangle_right_fill', 'square_fill', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
      ,15, 16, 17</td>
    </tr>

    <tr>
      <td><code>markercolor</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>markersize</code></td>

      <td>IntType: (Range 1 to 300)</td>
    </tr>

    <tr>
      <th><a name="vector"></a>Object: vector</td>

      <th>(graphics method
      class name is Gv)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>xaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>yaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
      2, 3, 4)</td>
    </tr>

    <tr>
      <td><code>linecolor</code></td>

      <td>ListType, TupleType (Values range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>scale</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>alignment</code></td>

      <td>Either: 'head', 'center', 'tail', 0, 1, 2</td>
    </tr>

    <tr>
      <td><code>type</code></td>

      <td>Either: 'arrows', 'barbs', 'solidarrows', 0, 1, 2</td>
    </tr>

    <tr>
      <td><code>reference</code></td>

      <td>FloatType, IntType</td>
    </tr>

    <tr>
      <th><a name="xvsy"></a>Object: xvsy</td>

      <th>(graphics method
      class name is GXY)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>xaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>yaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
      2, 3, 4)</td>
    </tr>

    <tr>
      <td><code>linecolor</code></td>

      <td>ListType, TupleType (Values range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>marker</code></td>

      <td>MarkerObject or (Either: 'dot', 'plus', 'star', 'circle', 'cross', 'diamond',
      'triangle_up', 'triangle_down', 'triangle_left', 'triangle_right', 'square',
      'diamond_fill', 'triangle_up_fill', 'triangle_down_fill', 'triangle_left_fill',
      'triangle_right_fill', 'square_fill', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
      ,15, 16, 17</td>
    </tr>

    <tr>
      <td><code>markercolor</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>markersize</code></td>

      <td>IntType: (Range 1 to 300)</td>
    </tr>

    <tr>
      <th><a name="xyvsy"></a>Object: xyvsy</td>

      <th>(graphics method
      class name is GXy)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>xaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
      2, 3, 4)</td>
    </tr>

    <tr>
      <td><code>linecolor</code></td>

      <td>ListType, TupleType (Values range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>marker</code></td>

      <td>MarkerObject or (Either: 'dot', 'plus', 'star', 'circle', 'cross', 'diamond',
      'triangle_up', 'triangle_down', 'triangle_left', 'triangle_right', 'square',
      'diamond_fill', 'triangle_up_fill', 'triangle_down_fill', 'triangle_left_fill',
      'triangle_right_fill', 'square_fill', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
      ,15, 16, 17</td>
    </tr>

    <tr>
      <td><code>markercolor</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>markersize</code></td>

      <td>IntType: (Range 1 to 300)</td>
    </tr>

    <tr>
      <th><a name="yxvsx"></a>Object: yxvsx</td>

      <th>(graphics method
      class name is GYx)</th>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>projection</code></td>

      <td>Either: linear , mollweide , robinson , or polar</td>
    </tr>

    <tr>
      <td><code>xticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>xmtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>yticlabels2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics1</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>ymtics2</code></td>

      <td>StringType or DictType</td>
    </tr>

    <tr>
      <td><code>datawc_x1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y1</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_x2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>datawc_y2</code></td>

      <td>IntType or FloatType</td>
    </tr>

    <tr>
      <td><code>yaxisconvert</code></td>

      <td>Either: 'linear', 'log10', 'ln','exp','area_wt'</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
      2, 3, 4)</td>
    </tr>

    <tr>
      <td><code>linecolor</code></td>

      <td>ListType, TupleType (Values range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>marker</code></td>

      <td>MarkerObject or (Either: 'dot', 'plus', 'star', 'circle', 'cross', 'diamond',
      'triangle_up', 'triangle_down', 'triangle_left', 'triangle_right', 'square',
      'diamond_fill', 'triangle_up_fill', 'triangle_down_fill', 'triangle_left_fill',
      'triangle_right_fill', 'square_fill', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
      ,15, 16, 17</td>
    </tr>

    <tr>
      <td><code>markercolor</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>markersize</code></td>

      <td>IntType: (Range 1 to 300)</td>
    </tr>

    <tr>
      <th><a name="template"></a>Object: template</td>

      <th>(Picture Template
      class name is P)</th>
    </tr>

    <tr>
      <td>Member: <code>file</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>function</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member:&nbsp;<code>logicalmask</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member:&nbsp;<code>transformation</code></td>

      <td></td>
    </tr>
    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>source</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>dataname</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>title</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>units</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>crdate</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>crtime</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>comment1</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>comment2</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>comment3</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>comment4</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>xname</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>yname</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>zname</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>tname</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>xunits</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>yunits</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>zunits</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>tunits</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>xvalue</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>format</code></td>

      <td>Currently not able to set</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>yvalue</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>format</code></td>

      <td>Currently not able to set</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>zvalue</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>format</code></td>

      <td>Currently not able to set</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>tvalue</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>format</code></td>

      <td>Currently not able to set</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>mean</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>format</code></td>

      <td>Currently not able to set</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>min</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>format</code></td>

      <td>Currently not able to set</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>max</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>format</code></td>

      <td>Currently not able to set</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>xtic1</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>xtic2</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>xmintic1</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>xmintic2</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>ytic1</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>ytic2</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>ymintic1</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>ymintic2</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>xlabel1</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>xlabel2</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>y</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>ylabel1</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>ylabel2</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>box1</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>box2</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>box3</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>box4</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>line1</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>line2</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>line3</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>line4</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>legend</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>line</code></td>

      <td>LineObject, StringType</td>
    </tr>

    <tr>
      <td><code>texttable</code></td>

      <td>TexttableObject, StringType</td>
    </tr>

    <tr>
      <td><code>textorientation</code></td>

      <td>TextorientationObject, StringType</td>
    </tr>

    <tr>
      <td>Member: <code>data</code></td>

      <td></td>
    </tr>

    <tr>
      <td><code>priority</code></td>

      <td>IntType</td>
    </tr>

    <tr>
      <td><code>x1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y1</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>x2</code></td>

      <td>IntType, FloatType</td>
    </tr>

    <tr>
      <td><code>y2</code></td>

      <td>IntType, FloatType</td>
    </tr>
  </table>



