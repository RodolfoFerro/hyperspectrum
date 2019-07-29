---
title: "Day 1:"
subtitle: >
  - Introduction to Physics of Light and Image Sensors <br>
  - Hyperspectral Cameras <br>
  - Introduction to Python
layout: page
show_sidebar: false
hide_footer: true
menubar: site_menu
---

# Introduction to Python

In this section we will learn the basics of Python and how to work with matrices.

# Title of content

This is a demo page showing some demo text.

We can also add some code snipets:
```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = np.linspace(-50, 50, 1000)
y = np.sin(x)

plt.figure(figsize=(10, 4))
plt.plot(x, y)
plt.savefig("plt_example.png")
```
<br>

And display images:

![plt_example.png](../assets/images/plt_example.png)

We can use these sections to attach any material (it can be a Google Colab notebook or whaterver we want).