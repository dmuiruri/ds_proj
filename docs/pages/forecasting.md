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

### Regression Results

#### industry

|    coef            |   std err    |    t     | P\>\|t\| | \[0.025   0.975\]  |
|:-------------------|:-------------|:---------|:-------- |:-------------------|
|P\:          1.6605 |    0.081     | 20.377   |  0.000   |  1.501      1.820  |
|U\:          3.1617 |    0.708     | 4.464    |  0.000   |  1.773      4.550  |
|Ff\:        13.4256 |    8.082     | 1.661    |  0.097   | -2.417     29.268  |
|Td\:       -10.3302 |    2.385     | -4.331   |  0.000   | -15.006     -5.655 |

|   R-Squared  | Adj. R-squared |  Durbin-Watson |  Jarque-Bera   |   Skew   | Kurtosis | No. Observation |
|:-------------|:---------------|:---------------|:---------------|:---------|:-------- |:-------|                                    
|   0.576      |    0.576       |    0.225       |  981.370       |   0.383  |   1.546  |  8717  |

This results indicate that the selected weather parameters are significant in explaining energy consumption in the industrial setting. However, in the overall the model has a relatively weak predicting power as seen from an R-squared 57.6% and high statistical value to the Jarque-Bera statistics. While these weather parameters can explain some of the variance in consumption a reasonable amount of variance is not accounted for by the model.

#### Commercial Building


### Model
$$
   |\psi_1\rangle = a|0\rangle + b|1\rangle
$$
Text can be **bold**, _italic_, or ~~strikethrough~~.

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.




[back](./../pages/forecasting.html)
