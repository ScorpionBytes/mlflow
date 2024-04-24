class Resource:
    def to_dict(self):
        raise NotImplementedError("Each resource must implement a to_dict method.")


class ChatEndpoint(Resource):
    def __init__(self, *endpoint):
        self.endpoint = list(endpoint)

    def to_dict(self):
        return {"databricks_chat_endpoint_name": self.endpoint}


class EmbeddingEndpoint(Resource):
    def __init__(self, *endpoint):
        self.endpoint = list(endpoint)

    def to_dict(self):
        return {"databricks_embeddings_endpoint_name": self.endpoint}


class VectorSearchEndpoint(Resource):
    def __init__(self, *endpoint):
        self.endpoint = list(endpoint)

    def to_dict(self):
        return {"databricks_vector_search_endpoint_name": self.endpoint}


class IndexName(Resource):
    def __init__(self, *index_names):
        self.index_name = list(index_names)

    def to_dict(self):
        return {"databricks_vector_search_index_name": self.index_name}


class DatabricksDependency(Resource):
    def __init__(self, chat=None, embeddings=None, vector_search=None, index=None):
        self.chat = chat
        self.embeddings = embeddings
        self.vector_search = vector_search
        self.index = index

    def to_dict(self):
        dependencies = {}
        if self.chat:
            dependencies.update(self.chat.to_dict())
        if self.embeddings:
            dependencies.update(self.embeddings.to_dict())
        if self.vector_search:
            dependencies.update(self.vector_search.to_dict())
        if self.index:
            dependencies.update(self.index.to_dict())
        return {"databricks-dependencies": dependencies}
