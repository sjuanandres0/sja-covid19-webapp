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
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv')
    df = df[df.iso_code.apply(lambda x: x[:5]!='OWID_')].copy()
    df['date'] = pd.to_datetime(df['date']) 
    co_focus = ['Argentina', 'Netherlands', 'United Kingdom', 'Spain', 'United States', 
                         'Turkey','India', 'Ireland', 'Vietnam','Brazil','Uruguay','Chile',
                         'Northern Ireland','Mexico','Germany','Ukraine']
    df = df[df.location.isin(co_focus)]

    graph_three = []
    for country in co_focus:
        graph_three.append(
          go.Scatter(
          x = df[df['location']==country]['date'],
          y = df[df['location']==country]['daily_vaccinations'],
          mode = 'lines',
          name = country
          )
        )

    layout_three = dict(title = '<b>Focus Countries Daily Vaccinations</b>',
                xaxis = dict(title = 'Date'),
                yaxis = dict(title = 'Daily Vaccinations')
                       )
    
# fourth chart shows rural population vs arable land
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv')
    df = df[df.iso_code.apply(lambda x: x[:5]!='OWID_')].copy()
    df['date'] = pd.to_datetime(df['date']) 
    co_focus = ['Argentina', 'Netherlands', 'United Kingdom', 'Spain', 'United States', 
                         'Turkey','India', 'Ireland', 'Vietnam','Brazil','Uruguay','Chile',
                         'Northern Ireland','Mexico','Germany','Ukraine']
    df = df[df.location.isin(co_focus)]

    graph_four = []
    
    for country in co_focus:
        graph_four.append(
          go.Scatter(
          x = df[df['location']==country]['date'],
          y = df[df['location']==country]['total_vaccinations_per_hundred'],
          mode = 'lines',
          name = country
          )
        )

    layout_four = dict(title = '<b>Focus Countries Daily Vaccinations per Hundred</b>',
                xaxis = dict(title = 'Date'),
                yaxis = dict(title = 'Daily Vaccinations per Hundred'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures