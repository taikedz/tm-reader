def html_summary_gen(articles:list[tuple[str,str,str,str]]):
    for art in articles:
        title, link, description, pubdate = art

        yield f"""
                <div class="article">
                    <p class="title"><a href="{link}" target="_blank">{title}</a></p>
                    <p class="gendate">{pubdate}</p>
                    <p class="description">{description}</p>
                </div>
                """
