from json import load
from requests import get
from i2amparis_main.models import *


def load_region_db():
    f = 'regions_dict.json'
    with open(f) as f:
            data = load(f)
    models = list(data.keys())
    for model in models:
        print(model)
        m = ModelsInfo.objects.get(model_title=model)
        regions = list(data[model].keys())
        for region in regions:
            if ',' in region:
                temp = region.lower()
                temp = [i.strip() for i in temp.split(',')]
                region_name = '_'.join(temp)
            else:
                temp = region.lower()
                temp = [i.strip() for i in temp.split(' ')]
                region_name = '_'.join(temp)
            if Regions.objects.filter(region_name = region_name).exists() == True:
                region_name = region+'_'+model
            if region != 'GLOBE':
                countries = data[model][region]
                descr = countries[-1]
                countries = countries[0]
            else:
                countries = case_of_global()
                descr = 'GLOBE'
            r = Regions(region_name=region_name,region_title=region, descr=descr)
            r.save()
            r.model_name.add(m)
            print(countries)
            for country in countries:
                print(country)
                [[country_name, country_code]] = country.items()
                if Countries.objects.filter(country_name=country_name).exists() == True:
                    c = Countries.objects.get(country_name=country_name)
                else:
                    c = Countries(country_name=country_name,country_code=country_code)
                    c.save()
                c.region_name.add(r)

def case_of_global():
    """
    :return:
    """
    # all_countries = get('https://restcountries.eu/rest/v2/all')
    # all_countries = all_countries.json()
    with open('global.json') as f:
        all_countries = load(f)
    data = []
    for i in all_countries:
        data.append(
            {i['name']: i['alpha2Code']}
        )
    return data







