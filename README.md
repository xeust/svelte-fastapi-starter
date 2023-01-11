## Development Server

1. Create a virtual env with `python3 -m venv .venv`
2. Navigate into the `svelte` directory and run `npm install`
3. From the top level directory, use `make dev` to start both dev servers thru uvicorn.
4. Develop away

## Publishing to Space

1. When you are ready to deploy, navigate into the `svelte` directory and run `npm run build`.
2. From the top level directory, run `space push`


