import string


def tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    return tokens


def build_index(documents):
    index = {}

    for document_id, document in documents.items():
        tokens = tokenize(document)

        for token in tokens:
            if token in index:
                index[token].add(document_id)
            else:
                index[token] = {document_id}

    return index

documents = {
    1: "The quick brown fox jumps over the lazy dog. Dogs love to play in the park.",
    2: "A brown fox is fast. The quick dog is not lazy!",
    3: "Information retrieval is the science of searching for information in a document. A document can contain text.",
    4: "Searching for a quick dog or a fast fox requires an inverted index. An index maps words to a document.",
    5: "The science of machine learning overlaps with information retrieval. Machine learning models process text fast.",
    6: "To play in the park, a dog must be fast and not lazy. The quick brown fox does not play in the park."
}

def query(user_input, index):
    tokens = tokenize(user_input)

    if not tokens:
        return set()

    if tokens[0] not in index:
        return set()

    results = index[tokens[0]]

    for token in tokens[1:]:
        if token not in index:
            return set()

        results = results & index[token]

    return results