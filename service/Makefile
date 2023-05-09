build_images:
	ssh root@135.181.204.59 "mkdir -p qa_system"
	scp -r qa-system/* root@135.181.204.59:~/qa_system/
	ssh root@135.181.204.59 "docker build -t localhost:5000/gateway ~/qa_system/gateway/"
	ssh root@135.181.204.59 "docker build -t localhost:5000/indexer ~/qa_system/indexer/"
	ssh root@135.181.204.59 "docker push localhost:5000/gateway"
	ssh root@135.181.204.59 "docker push localhost:5000/indexer"
	ssh root@65.108.144.165 "docker pull 135.181.204.59:5000/gateway"
	ssh root@65.108.144.165 "docker pull 135.181.204.59:5000/indexer"
send_index:
	ssh root@135.181.204.59 "mkdir -p /var/models/$(INDEX_GENERATION)/"
	scp -r qa_system/data/* root@135.181.204.59:/var/models/$(INDEX_GENERATION)/
	ssh root@65.108.144.165 "mkdir -p /var/models/$(INDEX_GENERATION)/"
	scp -r qa_system/data/* root@65.108.144.165:/var/models/$(INDEX_GENERATION)/
download_use_model:
	ssh root@135.181.204.59 "wget https://tfhub.dev/google/universal-sentence-encoder-multilingual/3?tf-hub-format=compressed -O use_model.tar.gz"
	ssh root@135.181.204.59 "mkdir -p qa_system/share/use_model/1 && tar -xf use_model.tar.gz -C qa_system/share/use_model/1"
	ssh root@65.108.144.165 "wget https://tfhub.dev/google/universal-sentence-encoder-multilingual/3?tf-hub-format=compressed -O use_model.tar.gz"
	ssh root@65.108.144.165 "mkdir -p qa_system/share/use_model/1 && tar -xf use_model.tar.gz -C qa_system/share/use_model/1"
start_app:
	ssh root@135.181.204.59 "docker stack deploy --compose-file ~/qa_system/docker-compose.yml qa_system"
stop_app:
	ssh root@135.181.204.59 "docker service rm qa_system_embedder qa_system_gateway qa_system_indexer_cl_0 qa_system_indexer_cl_1 qa_system_indexer_cl_2 qa_system_indexer_cl_3"
update_index:
	ssh root@65.108.144.165 "cp -r /var/models/$(INDEX_GENERATION)/* /root/qa_system/share/"
	ssh root@135.181.204.59 "cp -r /var/models/$(INDEX_GENERATION)/* /root/qa_system/share/"
	ssh root@135.181.204.59 "docker service update --force --update-delay 30s --update-failure-action=rollback qa_system_indexer_cl_0"
	ssh root@135.181.204.59 "docker service update --force --update-delay 30s --update-failure-action=rollback qa_system_indexer_cl_1"
	ssh root@135.181.204.59 "docker service update --force --update-delay 30s --update-failure-action=rollback qa_system_indexer_cl_2"
	ssh root@135.181.204.59 "docker service update --force --update-delay 30s --update-failure-action=rollback qa_system_indexer_cl_3"
	ssh root@135.181.204.59 "docker service update --force --update-delay 30s --update-failure-action=rollback qa_system_gateway"
