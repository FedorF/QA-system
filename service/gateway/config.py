import os


FLASK_HOST = '0.0.0.0'
FLASK_PORT = os.environ['FLASK_PORT']
INDEXER_URL = os.environ['INDEXER_URL']
EMBEDDER_URL = os.environ['EMBEDDER_URL']
CENTROIDS_PATH = os.environ['CENTROIDS_PATH']
VALID_CLUSTER_ID = ['0', '1', '2', '3']
