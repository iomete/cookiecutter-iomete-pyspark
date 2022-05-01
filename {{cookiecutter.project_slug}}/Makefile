docker_image := iomete/pyspark-job/job-template
docker_tag := 0.0.1

test:
	python setup.py test

docker-push:
	# Run this for one time: docker buildx create --use
	docker buildx build --platform linux/amd64,linux/arm64 --push -f docker/Dockerfile -t ${docker_image}:${docker_tag} .
	@echo ${docker_image}
	@echo ${docker_tag}
