import requests
class ScopusExtract:
    def __init__(self):
        self.api_key = None
        self.author_id = None

    def build_api_key(self, api_key):
        self.api_key = api_key
        return self

    def build_author_id(self, author_id):
        self.author_id = author_id
        return self

    def build(self):
        
        return self
    
    def _make_api_request(self, endpoint, params=None):
            base_url = ''
            headers = {'62abb09d6022337295084a7918b7': self.api_key}

            response = requests.get(base_url + endpoint, headers=headers, params=params)

            if response.status_code == 200:
                return response.json()
            else:
                # Handling API request error
                response.raise_for_status()

    def last_three_documents(self, author_name):
            endpoint = 'author/search'
            params = {'query': f'AUTHLASTNAME({author_name})', 'count': 3}
            response_data = self._make_api_request(endpoint, params)

            
            documents = response_data.get('search-results', {}).get('entry', [])
            return [{"title": "Document 1"}, {"title": "Document 2"}, {"title": "Document 3"}]
