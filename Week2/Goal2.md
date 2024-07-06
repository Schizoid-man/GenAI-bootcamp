 Use FASTAPI (Swagger) or Flask and have these endpoints:
  - Lookup(check-sentiment or classify-sentiment) (POST sentiment_text)
  - Similar_words(POST query_word and how many similar words you want)
	    - File system
	      - Annoy Index 
	      - connection pool
- deploy it as a docker container running on your local system
- use Postman to test the API service
## How do we scale this?
* Server Side caching
* Load balancer balances the load to your app servers
* Use cloudflare and then directs it to your servers so that it blocks out spam and DOS
* OWASP 
* Flood Testing

## Postgres for Annoy Indexes
Pgvector (neon.tech)
select (a.vector <cosine similarity> b.vector) as dist where a.word = "royal" order by dist and limit 100
