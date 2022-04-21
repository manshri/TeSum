from indicnlp.tokenize import indic_tokenize
from indicnlp.tokenize import sentence_tokenize
from blanc import BlancHelp, BlancTune
from bert_score import BERTScorer
import pandas as pd


# filter dataframe by value of given column with operand 'op'
def filter_frameCol(df, col, op, val):
    new_df = df.query(col + op + str(val))
    print("\n# Pairs with %s %s %d : "%(col, op, val), new_df.shape[0])
    print("# Invalid pairs: ", df.shape[0] - new_df.shape[0])
    return new_df

def rangeFilter_frameCol(df, cols, ops, vals):
    new_df = df.query(cols[0] + ops[0] + str(vals[0]) and cols[1] + ops[1] + str(vals[1]))
    print("\n# Pairs with %s %s %d and %s %s %d : "%(cols[0], ops[0], vals[0], cols[1], ops[1], vals[1]), new_df.shape[0])
    print("# Invalid pairs: ", df.shape[0] - new_df.shape[0])
    return new_df

def compFilter_frameCols(df, col1, op, col2, save=False):
    new_df = df.query(col1 + op + col2)
    print("\n# Pairs with %s %s %s : "%(col1, op, col2), new_df.shape[0])
    print("# Invalid pairs: ", df.shape[0] - new_df.shape[0])
    return new_df

"""# **Intrinsic Metrics Functions**"""

# ## Compute the set of Extractive Fragments F(A, S) (the set of shared sequences of tokens in A and S)

def F(A,S, ng=0):
    F = []
    i = j = 0
    i_hat = 0
    while i<len(S):
        f = []
        while j<len(A):
            if S[i]==A[j]:
                i_hat = i
                j_hat = j
                while i_hat<len(S) and j_hat<len(A) and S[i_hat] == A[j_hat]:
                    i_hat = i_hat + 1
                    j_hat = j_hat + 1
                if (i_hat-i) > ng and len(f)<(i_hat - i):
                    f = [S[n] for n in range(i, i_hat)]
                j = j_hat
            else:
                j = j + 1
        i = i + max(len(f),1)
        j = 0
        F.append(f)
    return set(tuple(e) for e in F)


# Compute compression & abstractivity scores for each pair
def add_Metrics(pairs, lang):

    modified_pairs = []
    count = 0
    xcount = 0
    F1_t_list = []
    F1_s_list = []

    for each in pairs:

        article_sents = sentence_tokenize.sentence_split(each['text'], lang='te')
        
        summary_tokens = indic_tokenize.trivial_tokenize(each['summary'])
        article_tokens = indic_tokenize.trivial_tokenize(each['text'])
        title_tokens = indic_tokenize.trivial_tokenize(each.get('title', ''))


        article_len = len(article_tokens)
        summary_len = len(summary_tokens)
        title_len = len(title_tokens)

        total_stokens = len(summary_tokens)
        
        # Compression
        compression = round((100 - (len(summary_tokens)/len(article_tokens))*100), 2)

        # Abstractivity
        sumF_abs = 0
        matched_fragments = F(article_tokens, summary_tokens, ng=0)
        for f in matched_fragments:
            sumF_abs += len(f)
        abstractivity = round((100 - (sumF_abs/total_stokens)*100), 2)

        new_pair = dict(each)
        new_pair.update({'article_sentence_count': len(article_sents), 'article_token_count': article_len, 'summary_token_count': summary_len, 'title_token_count': title_len, 'compression': compression, 'abstractivity': abstractivity})

        modified_pairs.append(new_pair)

    # Convert to DataFrame
    df = pd.DataFrame(modified_pairs)
    
    return df