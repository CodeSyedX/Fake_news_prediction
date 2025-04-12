import requests

def check_fact_google_fact_check(news_text, api_key):
    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        'query': news_text,
        'key': api_key,
        'languageCode': 'en'
    }
    
    response = requests.get(url, params=params)
    result = response.json()
    
    if 'claims' in result:
        for claim in result['claims']:
            print("🔹 Claim:", claim.get('text'))
            print("🔹 Rating:", claim['claimReview'][0].get('textualRating'))
            print("🔹 Publisher:", claim['claimReview'][0]['publisher'].get('name'))
            print("🔹 URL:", claim['claimReview'][0].get('url'))
            print("-" * 40)
    else:
        print("⚠️ No matching fact-checks found.")
