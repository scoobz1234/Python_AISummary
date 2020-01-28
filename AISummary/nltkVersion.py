import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer

'''
    # Tokenizing - word tokenizer's, and sentence tokenizer is grouping by these things
    # Corpora - body of text. ex: medical journals
    # Lexicon - words and their meanings
    # Stop Words - Words that can be removed typically and still keep sentence structure and meaning.
    # Stemming - Taking the stem from a word.
    # Part of Speech Tagging - 
'''
'''
Part of Speech tag list:

$: dollar    $ -$ --$ A$ C$ HK$ M$ NZ$ S$ U.S.$ US$                                                                             *
'': closing quotation mark ' ''                                                                                                                                     0
(: opening parenthesis ( [ {
): closing parenthesis ) ] }               
,: comma ,                                         
--: dash --
.: sentence terminator . ! ?
:: colon or ellipsis : ; ...

CC: conjunction, coordinating: &, 'n, and, both, but, either, et     
CD: numeral, cardinal: mid-1890, nine-thirty, forty-two     
DT: determiner: all, an, another, any, both 
EX: existential there: there    
FW: foreign word: gemeinschaft, hund, ich
IN: preposition or conjunction, subordinating: astride, among, whether    
JJ: adjective or numeral, ordinal: third, ill-mannered, pre-war,     
JJR: adjective, comparative: bleaker, braver, breezier, briefer,    
JJS: adjective, superlative: calmest, cheapest, choicest, classiest,
LS: list item marker: A A., B B., C C., D, E, F, First, G, H, I, J, K, One 
MD: modal auxiliary: can, cannot, could, couldn't, dare, may, might, must    
NN: noun, common, singular or mass: common-carrier, cabbage, knuckle-duster    
NNP: noun, proper, singular
    Motown Venneboerger Czestochwa Ranzer Conchita Trumplane Christos
    Oceanside Escobar Kreisler Sawyer Cougar Yvette Ervin ODI Darryl CTCA
    Shannon A.K.C. Meltex Liverpool ...
NNPS: noun, proper, plural

    Americans Americas Amharas Amityvilles Amusements Anarcho-Syndicalists
    Andalusians Andes Andruses Angels Animals Anthony Antilles Antiques
    Apache Apaches Apocrypha ...
NNS: noun, common, plural

    undergraduates scotches bric-a-brac products bodyguards facets coasts
    divestitures storehouses designs clubs fragrances averages
    subjectivists apprehensions muses factory-jobs ...
    
PDT: pre-determiner
    all both half many quite such sure this
    
POS: genitive marker
    ' 's
    
PRP: pronoun, personal
    hers herself him himself hisself it itself me myself one oneself ours
    ourselves ownself self she thee theirs them themselves they thou thy us
    
PRP$: pronoun, possessive
    her his mine my our ours their thy your
    
RB: adverb
    occasionally unabatingly maddeningly adventurously professedly
    stirringly prominently technologically magisterially predominately
    swiftly fiscally pitilessly ...
    
RBR: adverb, comparative
    further gloomier grander graver greater grimmer harder harsher
    healthier heavier higher however larger later leaner lengthier less-
    perfectly lesser lonelier longer louder lower more ...
    
RBS: adverb, superlative
    best biggest bluntest earliest farthest first furthest hardest
    heartiest highest largest least less most nearest second tightest worst
    
RP: particle
    aboard about across along apart around aside at away back before behind
    by crop down ever fast for forth from go high i.e. in into just later
    low more off on open out over per pie raising start teeth that through
    under unto up up-pp upon whole with you
    
SYM: symbol
    % & ' '' ''. ) ). * + ,. < = > @ A[fj] U.S U.S.S.R * ** ***
    
TO: "to" as preposition or infinitive marker
    to
    
UH: interjection
    Goodbye Goody Gosh Wow Jeepers Jee-sus Hubba Hey Kee-reist Oops amen
    huh howdy uh dammit whammo shucks heck anyways whodunnit honey golly
    man baby diddle hush sonuvabitch ...
    
VB: verb, base form
    ask assemble assess assign assume atone attention avoid bake balkanize
    bank begin behold believe bend benefit bevel beware bless boil bomb
    boost brace break bring broil brush build ...
    
VBD: verb, past tense
    dipped pleaded swiped regummed soaked tidied convened halted registered
    cushioned exacted snubbed strode aimed adopted belied figgered
    speculated wore appreciated contemplated ...
    
VBG: verb, present participle or gerund
    telegraphing stirring focusing angering judging stalling lactating
    hankerin' alleging veering capping approaching traveling besieging
    encrypting interrupting erasing wincing ...
    
VBN: verb, past participle
    multihulled dilapidated aerosolized chaired languished panelized used
    experimented flourished imitated reunifed factored condensed sheared
    unsettled primed dubbed desired ...
    
VBP: verb, present tense, not 3rd person singular
    predominate wrap resort sue twist spill cure lengthen brush terminate
    appear tend stray glisten obtain comprise detest tease attract
    emphasize mold postpone sever return wag ...
    
VBZ: verb, present tense, 3rd person singular
    bases reconstructs marks mixes displeases seals carps weaves snatches
    slumps stretches authorizes smolders pictures emerges stockpiles
    seduces fizzes uses bolsters slaps speaks pleads ...
    
WDT: WH-determiner
    that what whatever which whichever
    
WP: WH-pronoun
    that what whatever whatsoever which who whom whosoever
    
WP$: WH-pronoun, possessive
    whose
    
WRB: Wh-adverb
    how however whence whenever where whereby whereever wherein whereof why
    
``: opening quotation mark ` ``
'''

'''
Modifiers:
{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1
* = match 0 or more
$ = matches at the end of string
^ = matches at the start of a string
| = matches either/or
[] = range, or "variance
{x} = expect to see this amount of the preceding code
{x,y} = expect to see this x-y amounts of the preceding code
'''

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            namedEnt = nltk.ne_chunk(tagged)

            namedEnt.draw()

    except Exception as e:
        print(str(e))

process_content()