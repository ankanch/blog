export JEKYLL_VERSION=3.8
docker run --rm \
            -v "$(pwd)":/srv/jekyll \
            -p 1996:1996 \
            -it jekyll/jekyll:$JEKYLL_VERSION \
            jekyll serve --host 0.0.0.0 --watch --drafts --port 1996