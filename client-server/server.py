import yaml
from app.scopus_extract import ScopusExtract
from app.scopus_transform import ScopusTransform
from app.scopus_load import ScopusLoad

def main():
    conffile = "conf.json"
    with open(conffile, 'r') as f:
        conf = yaml.safe_load(f)
    
    # Building ScopusExtract instance
    scopus_extract = ScopusExtract() \
        .build_api_key(conf["api_key"]) \
        .build_author_id(conf["author_id"]) \
        .build()
    
    # Building ScopusTransform instance
    scopus_transform = ScopusTransform() \
        .build()
    
    # Building ScopusLoad instance
    scopus_load = ScopusLoad() \
        .build()
    
    # What are the last three documents of an author?
    author_name = "Lorenzo Carnevale"
    last_three_documents = scopus_extract.last_three_documents(author_name)
    last_three_documents_transformed = scopus_transform.documents(last_three_documents)
    print("Last three documents:")
    for document in last_three_documents_transformed:
        print(document)

    # What are the subject areas of an author?
    author_subject_areas = scopus_extract.author_subject_areas(author_name)
    author_subject_areas_transformed = scopus_transform.subject_areas(author_subject_areas)
    print("Subject areas:")
    for subject_area in author_subject_areas_transformed:
        print(subject_area)

    # What are the metrics of an author?
    author_metrics = scopus_extract.author_metrics(author_name)
    print("Metrics:", author_metrics)

    
    # scopus_load.load()

if __name__ == "__main__":
    main()
