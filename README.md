Run Svelte frontend + FastAPI backend on Deta Space.

## Directory Structure

The root of the project contains the Spacefile and two subdirectories, each running one Micro.

The `svelte` directory contains the SvelteKit frontend. The `fastapi` directory contains the FastAPI backend.

```txt
Spacefile
/svelte
  /src
  /static
  package.json
  ...
/fastapi
    main.py
    requirements.txt
    ...
```

## Development Server

1. Navigate into the fastapi directory and create a virtual env with `python3 -m venv .venv`.
2. Install all dependencies with `pip install -r requirements.txt`.
3. Navigate into the `svelte` directory and run `npm install`
4. From the top level directory, run `space dev` to start both servers through a single port.
5. Develop away

## Notes

Your `fastapi` server will now be served on the `/api` route, which is set in the `Spacefile`. Try visiting the development server's `/api` route to see it in action. The `/` route will serve the SvelteKit frontend.

## Publishing to Space

1. Run `space new`.
2. From the top level directory, run `space push` (first run `space new` if you have no Space project).


