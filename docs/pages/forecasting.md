---
layout: default
---

[Introduction](./../index.html) | [Correlation Analysis](./../pages/corr_analysis.html) | [Forecasting](./../pages/forecasting.html) | [Link to page 4](./pages/another-page.html)
In this section model the relationship between energy consumption and weather parameters where we hypothesise that weather has an impact on energy consumption in this particular location. Additionally, if weather does indeed affect energy consumption can a model be created to predit the same?

## Regression models
To setup the regression model, we first check the correlations between the regressors, as high correlation between them would lead to unstable parameters.

| -  |   T  |   P   |   U  |   Ff |   Td |
|:---|:-----|:------|:-----|------|:-----|
| T	 | 1,0	|     	|      |      |	     |
| P	 | 0,1	|  1,0	|      |     	|      |
| U	 | -0,7	| -0,2	| 1,0	 |    	|      |
| Ff | 0,1	| -0,3	| -0,2 |	1,0	|      |
| Td | 0,7	|  0,0	| 0,0	 | -0,1	|  1,0 |

Following the correlations listed in the table above it is evident that Temperature(T) has a high correlation with the Dew point temparature(Td) and humidity, Td however has a low correlation to U. It is therefore imperative that one the two measures of temperature be ommitted from the model.

# Header 1

Text can be **bold**, _italic_, or ~~strikethrough~~.

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://assets-cdn.github.com/images/icons/emoji/octocat.png)

### Just an image header H3

![This img is in assets/images folder](./assets/images/building.png)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```


This is one of the sub pages


[back](./../pages/forecasting.html)
