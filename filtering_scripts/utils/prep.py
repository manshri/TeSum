import re
import string
from . import utility as ut
from indicnlp.tokenize import sentence_tokenize


def basic_cleaning(data):
    data = data.replace("[!]+",". ").replace("\.{2,}",".").replace('\u200c','').replace('\u200b','').replace('\xa0',' ').replace('\x7f',' ').replace('\ufeff','').replace('\.+"+','"').replace('["]+',"")
    data = data.replace("\.+'+","'").replace('\.+\s*-+',', ').replace("[:\?\t]+"," ").replace("[\n]+","\n").replace("[\r]+","")
    data = data.replace('&', '').replace('&nbsp;', ' ')
    data = data.replace('\,+', ',')
    data = ' '.join(data.split())
    # data = data.replace('\?+', '')
    data = data.strip()
    return data


# Removes time stamps
def remove_timestamp(original_content):
    updated_content = re.sub(r'(First Published).\w+.\d+,.\d+,.\d+:\d+.\w+.IST', '', original_content)
    updated_content = re.sub(r'(Last Updated).*IST$', '', updated_content)
    updated_content = re.sub(r'\w+.\d+,.\d+,.\d+:\d+.\w+.IST', '', updated_content)
    return updated_content.strip()


# Remove punctuations and spaces
def remove_nonTelugu(content):
    updated_content = re.sub(r'[a-zA-Z0-9\s,\'\+\*_`~:."=<\@/>\-;]+', '', content)
    return updated_content


# Remove english words of more than 3 characters
def filter_english(content):
    updated_content = re.sub((r"([^\s][a-zA-Z]+\w*)"), ' ', content)
    return updated_content


def clean_text(pairs, config, save=False):
    ''' Clean all pairs:
        - Remove timestamps, english content and noise from article and summary text.
        - Save cleaned pairs if save=True.
    '''
    for pair in pairs:

        # if config.dataset == "tesum":
        #     article_content = pair['cleaned_text']
        # else:
        article_content = pair['text']
        updated_article_content = remove_timestamp(article_content)
        updated_article_content = filter_english(updated_article_content)
        updated_article_content = basic_cleaning(updated_article_content)
        # if config.dataset == "tesum":
        #     if 'text' in pair.keys():
        del pair['text']
        pair['cleaned_text'] = updated_article_content
        # else:
        #     pair['text'] = updated_article_content
        
        summary_content = pair['summary']
        updated_summary_content = remove_timestamp(summary_content)
        updated_summary_content = filter_english(updated_summary_content)
        updated_summary_content = basic_cleaning(updated_summary_content)
        pair['summary'] = updated_summary_content
    
    print(len(pairs), " pairs cleaned.")

    if save:
        clean_file = config.save_dir[config.dataset] + "cleaned_%s.jsonl"%config.dataset
        ut.write_finalPairs(clean_file, pairs)
    return pairs


# Find empty
def isEmptyPair(article, summary):
    if article.strip():
        if summary.strip():
            return False
    return True


# Find prefix pairs 
# (i.e. pairs where the summary is just Lead-N of the corresponding article)
def has_prefix(article_text, summary_text):
    
    # remove "<city_name>: " from the front
    article_text = re.sub(r'^.{1,15}:\s', '', article_text)
    summary_text = re.sub(r'^.{1,15}:\s', '', summary_text)
    
    # Check prefix only if article is longer than summary
    if len(article_text) >= len(summary_text):
            
        # remove non-Telugu chars
        summary_content = remove_nonTelugu(summary_text)  #, lang='te')
        article_content = remove_nonTelugu(article_text)  #, lang='te')

        if article_content.startswith(summary_content, 0):
            return True
        else:
            return False
    else:
        return False


# Apply basic filters to remove empty or duplicate pairs, and pairs with duplicate summaries or summary as prefixes...
def apply_basic_filters(all_pairs, config, save=False):

    ## Some sort of indexing of pairs is must
    attributes = all_pairs[0].keys()
    if 'index' in attributes or 'id' in attributes or 'url' in attributes:
        pass
    else:
        raise ValueError("No indexing found. \nAdd an id/index attribute.")

    empty_pairs = []
    prefixed_pairs = []
    duplicate_pairs = []
    duplicate_summary_pairs = []
    valid_pairs = []

    pairs_dictionary = {}
    summary_dictionary = {}

    dup_pair_count = 0
    dup_summ_count = 0

    for pair in all_pairs:
        article_content = remove_nonTelugu(pair['cleaned_text'])
        summary_content = remove_nonTelugu(pair['summary'])

        if not isEmptyPair(article_content, summary_content):  # if not empty pair
            pairText = article_content + '\t-@@@-\t' + summary_content

            if pairText in pairs_dictionary.keys():  # if already-seen pair (i.e. duplicate pair)
                if len(pairs_dictionary[pairText]) == 1:  # if first duplicate of the pairText found
                    duplicate_pairs.append(pairs_dictionary[pairText][0])  # add first copy to duplicates as well
                    pairs_dictionary[pairText].append(pair)  # add only one more pair as an indication of pair-redundancy
                duplicate_pairs.append(pair)
                dup_pair_count += 1

            elif summary_content in summary_dictionary:  # if already-seen summary or duplicate summary
                if len(summary_dictionary[summary_content]) == 1:  # if first duplicate of the summary_content found
                    duplicate_summary_pairs.append(summary_dictionary[summary_content][0])  # add first copy to duplicates as well
                    summary_dictionary[summary_content].append(pair)  # add only one more pair as an indication of summary-redundancy
                duplicate_summary_pairs.append(pair)
                dup_summ_count += 1

            else: # first-occurance-of-pair or unique pair
                pairs_dictionary[pairText] = [pair]  # book-keeping of each pair
                summary_dictionary[summary_content] = [pair] # book-keeping of each summary

                if not has_prefix(pair['cleaned_text'], pair['summary']):
                    valid_pairs.append(pair)  # final filtered pair
                else:
                    prefixed_pairs.append(pair)
        else:
            empty_pairs.append(pair)

    
    if save:
        # Save prefix IDs
        prefixID_file = config.save_dir[config.dataset] + 'prefixIDs_%s.txt'%config.dataset
        ut.saveIDs(prefixed_pairs, prefixID_file)

        # Save empty IDs
        emptyID_file = config.save_dir[config.dataset] + 'emptyIDs_%s.txt'%config.dataset
        ut.saveIDs(empty_pairs, emptyID_file)

        # Save duplicate pair IDs
        dupID_file = config.save_dir[config.dataset] + 'duplicateIDs_%s.txt'%config.dataset
        ut.saveIDs(duplicate_pairs, dupID_file)

        # Save duplicate summary IDs
        dupSummID_file = config.save_dir[config.dataset] + 'dupSummaryIDs_%s.txt'%config.dataset
        ut.saveIDs(duplicate_summary_pairs, dupSummID_file)

    print("\n# Empty article/summary/pairs: ", len(empty_pairs))
    print("# Duplicates pairs: ", len(duplicate_pairs), "\t #Extra copies: ", dup_pair_count)
    print("# Duplicate summaries: ", len(duplicate_summary_pairs), "\t #Extra copies: ", dup_summ_count)
    print("# Pairs with prefixes: ", len(prefixed_pairs))
    print("# Valid pairs: ", len(valid_pairs))

    return valid_pairs