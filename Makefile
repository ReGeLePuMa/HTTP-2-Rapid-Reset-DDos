DIRS := $(shell find -maxdepth 1 -mindepth 1 -type d ! -name ".*" -exec basename {} \;)

.PHONY: build clean $(DIRS)

build: $(DIRS)

$(DIRS):
	docker build -t infra/$@ $@

clean:
	docker image prune -af
