import json
import plotly.graph_objects as go

# JSON data
data = '''
{
  "Brazil": {
    "1901": 11991584,
    "1902": 11982916,
    "1903": 12217660,
    "1904": 12457332,
    "1905": 12821923,
    "1906": 14053776,
    "1907": 14059640,
    "1908": 13953465,
    "1909": 15075522,
    "1910": 15240176,
    "1911": 16924502,
    "1912": 16727296,
    "1913": 17129840,
    "1914": 16816056,
    "1915": 17567888,
    "1916": 18091446,
    "1917": 19324732,
    "1918": 18945717,
    "1919": 21441165,
    "1920": 23567440,
    "1921": 24053340,
    "1922": 25716342,
    "1923": 27174558,
    "1924": 27166822,
    "1925": 27268468,
    "1926": 27857700,
    "1927": 29881302,
    "1928": 33329956,
    "1929": 33387410,
    "1930": 31419648,
    "1931": 30693376,
    "1932": 31775913,
    "1933": 34246080,
    "1934": 37132080,
    "1935": 38115900,
    "1936": 41777922,
    "1937": 43174692,
    "1938": 44967720,
    "1939": 45405703,
    "1940": 45842110,
    "1941": 49094523,
    "1942": 47246693,
    "1943": 53837553,
    "1944": 55839417,
    "1945": 57352815,
    "1946": 63399420,
    "1947": 65633490,
    "1948": 72004680,
    "1949": 77524263,
    "1950": 82783207,
    "1951": 84913824,
    "1952": 92376096,
    "1953": 96721560,
    "1954": 104800783,
    "1955": 114652544,
    "1956": 117655568,
    "1957": 125399063,
    "1958": 139050447,
    "1959": 147787920,
    "1960": 163464600,
    "1961": 180300186,
    "1962": 194583801,
    "1963": 197280523,
    "1964": 203845509,
    "1965": 208480337,
    "1966": 224672682,
    "1967": 241080900,
    "1968": 263736928,
    "1969": 276176124,
    "1970": 313365100,
    "1971": 351395640,
    "1972": 393307726,
    "1973": 444174283,
    "1974": 482066280,
    "1975": 505089681,
    "1976": 547301112,
    "1977": 560770819,
    "1978": 583222032,
    "1979": 622603584,
    "1980": 621497040,
    "1981": 646716936,
    "1982": 666042536,
    "1983": 658084520,
    "1984": 679017659,
    "1985": 715348074,
    "1986": 818043660,
    "1987": 840998760,
    "1988": 844896416,
    "1989": 866979288,
    "1990": 853656990,
    "1991": 907190235,
    "1992": 937529719,
    "1993": 1009891867,
    "1994": 1137516677,
    "1995": 1322510787,
    "1996": 1579907000,
    "1997": 1539679526,
    "1998": 1483776537,
    "1999": 1439213081,
    "2000": 1466684604,
    "2001": 1464612124,
    "2002": 1484978040,
    "2003": 1476516296,
    "2004": 1555839810,
    "2005": 1625963468,
    "2006": 1774804752,
    "2007": 1974875712,
    "2008": 2206760688,
    "2009": 2296768500,
    "2010": 2658669356,
    "2011": 2965072844,
    "2012": 2964952340,
    "2013": 3039077454,
    "2014": 3039792125,
    "2015": 3177918459,
    "2016": 2806988271
  }
}
'''

# Parse JSON data
parsed_data = json.loads(data)

# Extract years and population values for Brazil
years = list(parsed_data['Brazil'].keys())
populations = list(parsed_data['Brazil'].values())

# Create an interactive bar chart using Plotly
fig = go.Figure(data=[go.Bar(
    x=years,
    y=populations,
    marker=dict(color='rgb(138, 174, 235)', line=dict(color='rgb(8, 8, 97)', width=1.5)),
)])

# Update chart layout for better aesthetics
fig.update_layout(
    title='Annual GDP of Brazil Over Time',
    xaxis=dict(title='Year'),
    yaxis=dict(title='GDP'),
    plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent
    showlegend=False,  # Hide legend
)

# Save the chart as an HTML file
fig.write_html('index.html')
