import requests
from IPython.display import display, HTML

API_KEY = "65ab5c61c86be48dc53215e49d57f4a1"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

def get_movies(endpoint, params={}):
    url = f"{BASE_URL}/{endpoint}"
    params["api_key"] = API_KEY
    params["language"] = "pt-BR"
    r = requests.get(url, params=params)
    return r.json().get("results", [])

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY, "language": "pt-BR"}
    r = requests.get(url, params=params)
    return r.json()

def render_netflix_ui(sections):
    style = """
    <style>
      body { background:#141414; color:white; font-family:Arial; }
      .navbar { padding:20px; font-size:28px; font-weight:bold; color:#e50914; background:#000; }
      .section { margin:20px; }
      .section h3 { margin:10px 0; font-size:20px; }
      .row { display:flex; overflow-x:auto; scrollbar-width:none; }
      .row::-webkit-scrollbar { display:none; }
      .card {
        min-width:150px; height:220px; margin-right:10px; border-radius:6px;
        background-size:cover; background-position:center; flex-shrink:0;
        transition:transform 0.3s; cursor:pointer; position:relative;
      }
      .card:hover { transform:scale(1.08); }
      .card span {
        position:absolute; bottom:5px; left:5px; font-size:12px;
        background:rgba(0,0,0,0.6); padding:2px 5px; border-radius:3px;
      }
    </style>
    """
    html = '<div class="navbar">Netflix</div>'
    for section, items in sections.items():
        html += f'<div class="section"><h3>{section}</h3><div class="row">'
        for item in items:
            html += f"""
            <div class="card" style="background-image:url('{item['img']}');">
              <span>{item['title']}</span>
            </div>
            """
        html += '</div></div>'
    display(HTML(style + html))
