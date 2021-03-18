import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def get_and_sort(sort_by):
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv')
    df = df[df.iso_code.apply(lambda x: x[:5]!='OWID_')].copy()
    df = df.groupby('location').max().reset_index().sort_values(by=sort_by,ascending=False)
    return df

def return_figures():
    """Creates four plotly visualizations
    Args:
        None
    Returns:
        list (dict): list containing the four plotly visualizations
    """

#   first plot
#    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv')
#    df = df[df.iso_code.apply(lambda x: x[:5]!='OWID_')].copy()
#    df = df.groupby('location').max().reset_index().sort_values(by='total_vaccinations',ascending=False)
    
    df = get_and_sort('total_vaccinations')
    graph_one = []    
    graph_one.append(
      go.Bar(
      x = df['location'][:10],
      y = df['total_vaccinations'][:10],
      )
    )

    layout_one = dict(title = '<b>Top 10 Countries in Vaccinations</b>',
                xaxis = dict(title = 'Country'),
                yaxis = dict(title = 'Total Vaccinations'),
                )

# second chart     
    df = get_and_sort('total_vaccinations_per_hundred')
    graph_two = []    
    graph_two.append(
      go.Bar(
      x = df['location'][:10],
      y = df['total_vaccinations_per_hundred'][:10],
      )
    )

    layout_two = dict(title = '<b>Top 10 Countries in Vaccinations per hundred</b>',
                xaxis = dict(title = 'Country'),
                yaxis = dict(title = 'Total Vaccinations per hundred'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = [5, 4, 3, 2, 1, 0],
      y = [0, 2, 4, 6, 8, 10],
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Chart Three',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    
    graph_four.append(
      go.Scatter(
      x = [20, 40, 60, 80],
      y = [10, 20, 30, 40],
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Chart Four',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures