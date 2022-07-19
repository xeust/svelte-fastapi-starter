MAKEFLAGS+="-j 2"

.PHONY: all
all: dev

dev-server:
	uvicorn main:app --reload

dev-client:
	cd svelte && npm run dev

dev: dev-client dev-server