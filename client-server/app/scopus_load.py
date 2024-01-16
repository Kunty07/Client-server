
class ScopusLoad:
    def __init__(self):
        pass

    def build(self):
        
        return self

    def load(self, transformed_data):
        
        for doc in transformed_data:
            print(f"Loading: {doc['title']}")
