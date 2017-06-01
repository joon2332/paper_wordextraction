def idx_sampling(corpus_fnames, n_samples=1000):
    def close_all(files):
        for f in files:
            f.close()
    def open_all(corpus_fnames):
        return [open(corpus_fname, encoding='utf-8') for corpus_fname in corpus_fnames]
    def min_length(corpus_fnames):
        files = open_all(corpus_fnames)
        length = 0
        for f in files:
            for n_doc, _ in enumerate(f):
                continue
            length = n_doc if length == 0 else min(length, n_doc)
        return length
    def not_empty_all(docs):
        for doc in docs:
            if not (doc.strip()):
                return False
        return True
        
    import numpy as np
    
    m = min_length(corpus_fnames)
    samples = sorted(np.random.permutation(m)[:n_samples])
    return samples

def news_sampling(corpus_fnames, shared_index_fname, n_samples=1000):
    def open_all(corpus_fnames):
        return [open(corpus_fname, encoding='utf-8') for corpus_fname in corpus_fnames]
    
    samples = [0] + idx_sampling(corpus_fnames, n_samples)
    steps = [n-p for n, p in zip(samples[1:], samples)]
    files = open_all(corpus_fnames + [shared_index_fname])
    for step in steps:
        docs = []
        for f in files:
            for s in range(step-1):                
                next(f)
            docs.append(next(f))
        yield docs