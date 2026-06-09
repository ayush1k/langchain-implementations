from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader('Social_Network_Ads.csv')
docs = loader.load()
print(docs)