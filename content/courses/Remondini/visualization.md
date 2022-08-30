<!-- vscode-markdown-toc -->
* 1. [Learn](#Learn)
* 2. [Quiz](#Quiz)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->---
title: Visualization
date: '2021-01-01'
type: book
weight: 30
highlight: true
---


Learn how to visualize data with Plotly.

<!--more-->

{{< icon name="clock" pack="fas" >}} 1-2 hours per week, for 8 weeks

##  1. <a name='Learn'></a>Learn

{{< youtube hSPmj7mK6ng >}}

##  2. <a name='Quiz'></a>Quiz

{{< spoiler text="When is a heatmap useful?" >}}
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
{{< /spoiler >}}

{{< spoiler text="Write Plotly code to render a bar chart" >}}
```python
import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.show()
```
{{< /spoiler >}}
