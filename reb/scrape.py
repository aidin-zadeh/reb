

from reb.src import pynyt
from reb.conf import APIKEY_NYT_ARTICLE

nyt = pynyt.ArticleSearch(APIKEY_NYT_ARTICLE)
nytArchive = pynyt.ArchiveApi(APIKEY_NYT_ARTICLE)

# # get 1000 news articles from the Foreign newsdesk from 1987
# results_obama = nyt.query(
#     q='obama',
#     begin_date="20170101",
#     end_date="20170102",
#     # facet_field=['source', 'day_of_week'],
#     # facet_filter = True,
#     verbose=True)

arch = nytArchive.query(
    year="2012",
    month="1"
)