import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Store API response in a variable
response_dict = r.json()

print(f'Total repositories:{response_dict["total_count"]}')

# Explore information about the repositories
# &
# Process results
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')
for repo in repo_dicts:
    print('\nSelected information about the first repository:')
    print(f'Name: {repo["name"]}')
    print(f'Owner: {repo["owner"]["login"]}')
    print(f'Stars: {repo["stargazers_count"]}')
    print(f'Repository: {repo["html_url"]}')
    print(f'Created: {repo["created_at"]}')
    print(f'Updated: {repo["updated_at"]}')
    print(f'Description: {repo["description"]}')

stars, labels, repo_links = [], [], []
for repo in repo_dicts:
    repo_name = repo["name"]
    repo_stars = repo["stargazers_count"]
    stars.append(repo_stars)

    description = repo["description"]
    owner = repo["owner"]["login"]
    label = f"{owner}<br />{description}"
    labels.append(label)

    repo_url = repo["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
# Make visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects On Github',
    'xaxis': {'title': 'Repository',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14},
              },
    'yaxis': {'title': 'Stars',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14},
              }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
