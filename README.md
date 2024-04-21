Create **custom text2vec-transformers** embeddings using SentenceTransformer('all-MiniLM-L6-v2') hugginface model alternative to **text2vec-openai** 
1. start app.py server
2. run docker container
   docker run -d --name weaviate -p 28080:8080 -e ENABLE_MODULES=text2vec-transformers -e TRANSFORMERS_INFERENCE_API=http://host.docker.internal:7000/encode semitechnologies/weaviate:latest
3. Test text2vec-transformers using weaviate.ipynb
   
