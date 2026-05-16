/*
Stop words
Stop words list from http://www.ranks.nl/stopwords
*/

var tipuesearch_stop_words = ["a", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"];

// Word replace

var tipuesearch_replace = {"words": [
	{"word": "javscript", "replace_with": "javascript"},
	{"word": "jqeury", "replace_with": "jquery"}
]};

// Weighting

var tipuesearch_weight = {"weight": [
	{"url": "http://it.daniloquium.xyz", "score": 60},
	{"url": "http://it.daniloquium.xyz/su-di-me", "score": 40},
	{"url": "http://it.daniloquium.xyz/risorse", "score": 20}
]};

// Illogical stemming

var tipuesearch_stem = {"words": [
	{"word": "e-mail", "stem": "email"},
	{"word": "verbo", "stem": "verbi"}
]};

// Related

var tipuesearch_related = {"Related": [
	{"search": "essere", "related": "verbi", "include": 1}
]};

// Internal strings

var tipuesearch_string_1 = "Senza titolo"; // "No title";
var tipuesearch_string_2 = "Mostrando i risultati per"; // "Showing results for";
var tipuesearch_string_3 = "Cerca invece"; // "Search instead for";
var tipuesearch_string_4 = "1 risultado"; // "1 result";
var tipuesearch_string_5 = "risultati"; // "results";
var tipuesearch_string_6 = "<";
var tipuesearch_string_7 = ">";
var tipuesearch_string_8 = "Non è stato trovato nulla."; // "Nothing found.";
var tipuesearch_string_9 = "Le parole comuni sono in gran parte ignorate."; // "Common words are largely ignored.";
var tipuesearch_string_10 = "Correlato"; // "Related";
var tipuesearch_string_11 = "Ricerca troppo breve. Dovrebbe essere uno o più caratteri."; // "Search too short. Should be one character or more.";
var tipuesearch_string_12 = "Ricerca troppo breve. Dovrebbe essere"; // "Search too short. Should be";
var tipuesearch_string_13 = "o più caratteri."; // "characters or more.";
var tipuesearch_string_14 = "secondi"; // "seconds";
var tipuesearch_string_15 = "Apri immagine"; // "Open image";
var tipuesearch_string_16 = "Vai alla pagina"; // "Go to page";

// Internals

// Timer for showTime

var startTimer = new Date().getTime();
