export JEKYLL_VERSION=3.8
docker run --rm \
	  --volume="$PWD/blog_src:/srv/jekyll" \
	    -it jekyll/jekyll:$JEKYLL_VERSION \
		jekyll build