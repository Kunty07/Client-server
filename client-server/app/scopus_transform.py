
class ScopusTransform:
    def __init__(self):
        pass

    def build(self):
    
        return self

    def documents(self, raw_documents):
        
        return [{"title": f"Transformed - {doc['title']}"} for doc in raw_documents]
