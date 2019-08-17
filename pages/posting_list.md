---
title: postings
layout: global
permalink: /posts
---
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- aka kanch底部 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-6425922486772410"
     data-ad-slot="4055073289"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
<div class="cupcakes">
    {% for post in site.posts %}
      <div class="cupcake">
        <h2>{{ cupcake.type }}</h2>
        <a href="{{ site.baseurl }}{{ post.url }}" target="_blank">{{ post.date | date_to_string }} - {{ post.title }}</a>
        <p>{{ cupcake.description }}</p>
      </div>
    {% endfor %}
</div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- aka kanch底部 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-6425922486772410"
     data-ad-slot="4055073289"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
