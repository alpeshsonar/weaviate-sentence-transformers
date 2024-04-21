1. start app.py server
2. rnd docker container 
  docker run -d --name weaviate -p 28080:8080 -e ENABLE_MODULES=text2vec-transformers -e TRANSFORMERS_INFERENCE_API=http://host.docker.internal:7000/encode semitechnologies/weaviate:latest
4. Test text2vec-transformers using weaviate.ipynb
