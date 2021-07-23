```python
import pandas as pd 
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "png"
```


```python
world_data = pd.read_csv('../Data/our-world-can.csv')
world_data = world_data.rename(columns={'Entity': 'Country', 'total_tests': 'Number of Tests Performed', \
'142601-annotations': 'Tested T/F', 'Total confirmed deaths due to COVID-19': 'Deaths', 'Total confirmed cases of COVID-19': 'Cases'})

can = world_data[world_data['Country'] == 'Canada']
usa = world_data[world_data['Country'] == 'United States']
usa = usa.drop([98765,98764,98763,98762])
```


```python
world_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Entity</th>
      <th>Code</th>
      <th>Day</th>
      <th>total_tests</th>
      <th>142601-annotations</th>
      <th>Total confirmed deaths due to COVID-19</th>
      <th>Total confirmed cases of COVID-19</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020 Summer Olympics athletes &amp; staff</td>
      <td>NaN</td>
      <td>2021-06-19</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2020 Summer Olympics athletes &amp; staff</td>
      <td>NaN</td>
      <td>2021-06-20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2020 Summer Olympics athletes &amp; staff</td>
      <td>NaN</td>
      <td>2021-06-21</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020 Summer Olympics athletes &amp; staff</td>
      <td>NaN</td>
      <td>2021-06-22</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020 Summer Olympics athletes &amp; staff</td>
      <td>NaN</td>
      <td>2021-06-23</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>105718</th>
      <td>Zimbabwe</td>
      <td>ZWE</td>
      <td>2021-07-19</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2697.0</td>
      <td>85732.0</td>
    </tr>
    <tr>
      <th>105719</th>
      <td>Zimbabwe</td>
      <td>ZWE</td>
      <td>2021-07-20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2747.0</td>
      <td>88415.0</td>
    </tr>
    <tr>
      <th>105720</th>
      <td>Zimbabwe</td>
      <td>ZWE</td>
      <td>2020-03-20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>105721</th>
      <td>Zimbabwe</td>
      <td>ZWE</td>
      <td>2020-03-21</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>105722</th>
      <td>Zimbabwe</td>
      <td>ZWE</td>
      <td>2020-03-22</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
<p>105723 rows × 7 columns</p>
</div>




```python

```
