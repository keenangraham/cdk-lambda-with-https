import requests
import openai


def handler(event, context):
    print(event)

    query = event.get('queryStringParameters', {}).get('query')

    search_term = f'&searchTerm={query}' if query else ''

    response = requests.get(
        'https://www.encodeproject.org/search/?type=Award'
        '&field=description&field=lab&field=pi.lab.title'
        '&format=json&limit=3' + search_term
    )

    results = response.json()['@graph']

    if bool(event.get('queryStringParameters', {}).get('summarize')):



        results = []

        for award in response.json()['@graph']:
            prompt = award['description'] + ' tl;dr:'
            summary = openai.Completion.create(
                model='text-davinci-003',
                prompt=prompt,
                temperature=0.7,
                max_tokens=200,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=1
            )
            results.append(
                {
                    'summary': summary['choices'][0]['text'],
                    'original': award
                }
            )

    return {
        'message': 'ok',
        'results': results
    }
