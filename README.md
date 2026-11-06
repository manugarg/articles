# articles

Source for [articles.manugarg.com](https://articles.manugarg.com): Manu Garg's
projects page and a collection of technical articles, mostly on Linux and
networking internals.

## How it's served

- The site is built by **GitHub Pages** (Jekyll) from the `main` branch, root
  directory. Pushing to `main` deploys.
- The custom domain is set by the `CNAME` file. **Cloudflare** sits in front
  and handles HTTPS, so "Enforce HTTPS" is deliberately left off in the GitHub
  Pages settings.

## Layout

| Path | What it is |
| --- | --- |
| `index.html` | Landing page listing projects and articles |
| `*.html` | Articles, each with Jekyll front matter (`title`, `sharing`, `url`) |
| `*.pdf`, `*.ppt` | Articles only available as documents |
| `stack.txt`, `socket.txt` | Original plain-text versions of the stack and socket articles, kept so old links still work |
| `_includes/` | Shared header, footer, CSS, Google Analytics, and social sharing snippets |
| `_config.yml` | Site settings (author, URL, sharing options) |
| `sitemap.xml` | Sitemap for search engines |

## Adding an article

1. Create `<name>.html` at the top level, starting with front matter:

   ```yaml
   ---
   title: My Article
   sharing: true
   url: /my_article.html
   ---
   ```

   Use `{% include header.html %}` in `<head>` and follow an existing article
   for the rest of the structure.
2. Link it from `index.html` and add it to `sitemap.xml`.

## Previewing locally

```sh
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

## History

The site originally ran on Google App Engine (2010–2015). In 2015 it moved to
GitHub Pages on a `gh-pages` branch, while the old App Engine version stayed
on `master`. In 2026 the two were consolidated: `gh-pages` became `main` and
`master` was deleted. The last App Engine version is preserved under the tag
`legacy-appengine`.
