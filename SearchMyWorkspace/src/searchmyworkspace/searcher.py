import pysolr

class Searcher(object):
    """ Used to search Solr Index """
    def __init__(self, query):
        self.query = query

    def search(self):
        # Setup a Solr instance. The timeout is optional.
        solr = pysolr.Solr('http://localhost:8983/solr/mytc', timeout=10)
        results = solr.search(self.query)

        print("Saw {0} result(s).".format(len(results)))
        for result in results:
            print(result['title'])
            
        return results