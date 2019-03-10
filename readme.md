#Notes

Fork of [emanuil-tolev/intro-es-django-workshop](https://github.com/emanuil-tolev/intro-es-django-workshop)

###Elasticsearch installation
1. download ES from https://www.elastic.co/downloads/elasticsearch
2. `tar -xzf elasticsearch-6.6.1.tar.gz`
3. run ES: `./elasticsearch-6.6.1/bin/elasticsearch`
4. check `curl -XGET http://localhost:9200`

###How to
* create virtual environment from `requirements.txt`
* run Django shell `python manage.py shell`
```python
>>> from hotchoc.search import *
>>> hc = models.HotChocStore.objects.create(name='Berlin Choco Store', location='Berlin', description='blahblah', suggester='Enrica')
>>> hc = models.HotChocStore.objects.create(name='London Choco Store', location='London', description='blahblah2', suggester='Ema')
>>> hc.indexing()
>>> search(suggester='enrica')
>>> search(suggester='enrica')[0].name
'Berlin Choco Store'
```
* browser, go to: `http://localhost:9200/_search?q=suggester:enrica`
