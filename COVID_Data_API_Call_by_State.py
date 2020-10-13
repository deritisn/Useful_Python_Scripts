import requests
import json

def COVID_API():
    URL = 'https://localcoviddata.com/covid19/v1/cases/covidTracking'
    parameters = {'state' : input("Which state do you want COVID-19 data for? \n(Enter the state's capitalized two letter code) "), 'daysInPast': 1}
    response = requests.get(URL, params= parameters)
    print(response.url)
    content = response.content
    info = json.loads(content)

    state = info['stateName']
    yesterday = info['historicData']
    itemInfo = yesterday[0]
    positives = itemInfo['peoplePositiveCasesCt']
    new_positives = itemInfo['peoplePositiveNewCasesCt']
    negatives = itemInfo['peopleNegativeCasesCt']
    deaths = itemInfo['peopleDeathCt']
    date = itemInfo['date']
    new_deaths = itemInfo['peopleDeathNewCt']

    print('COVID-19 data for the state of {}'.format(state))
    print('This data is accurate as of {}'.format(date))
    print('Total Positive Cases: {}'.format(positives))
    print('New Positive Cases on {}: {}'.format(date, new_positives))
    print('Total Negative Cases: {}'.format(negatives))
    print('Total Deaths: {}'.format(deaths))
    print('New Deaths on {}: {}'.format(date, new_deaths))

COVID_API()
