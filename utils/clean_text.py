import re
from nltk.corpus import stopwords
import nltk

# Ensure stopwords are downloaded
nltk.download('stopwords')

# Dictionary for fixing encoding issues
CHARACTER_FIXES = {
    'ä±': 'ı', 'ÅŸ': 'ş', 'ã‡': 'ş', 'ã§': 'ç',
    'ã¼': 'ü', 'äÿ': 'ğ', 'åÿ': 'ş', 'ã¶': 'ö',
    'ã–': 'ö', 'â ': '', 'ðÿ': '', 'ðy': '', 'ð': '',
    'â‚º': '₺', 'Ä°': 'İ', 'Ã¢': 'â', 'Â': '',
    'Ãœ': 'Ü', 'Ã¶': 'ö', 'Ã§': 'ç', 'ÄŸ': 'ğ',
    'Ã¼': 'ü', 'Ä±': 'ı', 'â€™': '’', 'hÃ¢lÃ¢': 'hâlâ',
    'Ä°lkÂ': 'İlk', 'TÃœRKÄ°YE': 'TÜRKİYE', 'tãœrkä ye': 'türkiye',
    'ÿ': '',
}

# Define stopwords and additional words to remove
TURKISH_STOPWORDS = set(stopwords.words('turkish'))
ADDITIONAL_STOPWORDS = {
    'httpstco', 'en', 'daha', 'o', '?', 'kadar', 'gibi', ',', '.', 
    'bile', ':', '@', '\n', '..', '...', 'ya', 'yani', 'hiç', 'hala',
    'retweeted', 'Retweeted', 'retweet', 'retweets'
}
ALL_STOPWORDS = TURKISH_STOPWORDS.union(ADDITIONAL_STOPWORDS)

# Compile regex patterns
STOPWORDS_PATTERN = r'\b(?:{})\b'.format('|'.join(map(re.escape, ALL_STOPWORDS)))
LINKS_PATTERN = r"https?://\S+|www\.\S+|https\s*t\s*co\s*\S+"  # Remove links
MENTIONS_PATTERN = r"@\w+"  # Remove @mentions
REPEATED_LETTERS_PATTERN = r"(.)\1{2,}"  # Replace 3+ repeated letters

def clean_text(text):
    """
    Cleans text for analysis by:
    - Converting to lowercase.
    - Fixing Turkish encoding issues (e.g., 'hÃ¢lÃ¢' → 'hâlâ', 'TÃœRKÄ°YE' → 'TÜRKİYE').
    - Removing tweets that contain "Retweeted" or "retweeted".
    - Removing links (e.g., "https t co xyz").
    - Removing @mentions (e.g., "@username" → "").
    - Removing punctuation and special characters.
    - Removing Turkish stopwords and additional context-specific stopwords.
    - Fixing over-repeated letters (e.g., "sürprizzzz" → "sürpriz").
    - Removing extra spaces and newlines.

    Args:
        text (str): The input text.

    Returns:
        str: The cleaned text.
    """
    if not isinstance(text, str):
        return ""

    text = text.lower()  # Convert to lowercase

    # Remove links
    text = re.sub(LINKS_PATTERN, ' ', text)

    # Remove @mentions
    text = re.sub(MENTIONS_PATTERN, ' ', text)

    # Replace incorrectly encoded characters
    for bad_char, good_char in CHARACTER_FIXES.items():
        text = text.replace(bad_char, good_char)

    # Remove tweets that contain "Retweeted"
    if "retweeted" in text or "Retweeted" in text:
        return ""

    # Remove punctuation (keep words and spaces)
    text = re.sub(r'[^\w\s]', ' ', text)

    # Remove Turkish and additional stopwords
    text = re.sub(STOPWORDS_PATTERN, ' ', text)

    # Fix over-repeated letters (e.g., "sürprizzzz" → "sürpriz")
    text = re.sub(REPEATED_LETTERS_PATTERN, r'\1', text)

    # Remove extra spaces and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text