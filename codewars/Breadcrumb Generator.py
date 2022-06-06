# https://www.codewars.com/kata/breadcrumb-generator/train/python
import re


ignored_acronyms = [
    "the",
    "of",
    "in",
    "from",
    "by",
    "with",
    "and",
    "or",
    "for",
    "to",
    "at",
    "a",
]


def shorten(long_crumb):
    return "".join(
        [
            crumb[0].upper()
            for crumb in long_crumb.split("-")
            if crumb not in ignored_acronyms
        ]
    )


def render(url, full_url=[], is_last=False):
    content = shorten(url) if len(url) > 30 else " ".join(url.split("-")).upper()
    if is_last:
        content = re.split(r"(#|\?|\.)", content)[0]
        return f'<span class="active">{content}</span>'
    full_url = "/" + "/".join(full_url) + "/" if len(full_url) else "/"
    return f'<a href="{full_url}">{content}</a>'


def generate_bc(url, separator=" / "):
    crumbs = [
        crumb
        for crumb in re.split(r".\w+/", url, 1)[1].split("/")
        if crumb != "" and not crumb.startswith("index")
    ]
    crumb_links = [render("home")]
    if len(crumbs) == 0:
        return [render("home", is_last=True)]
    for i, crumb in enumerate(crumbs):
        crumb_links.append(
            render(crumb, crumbs[: i + 1], is_last=(i == len(crumbs) - 1))
        )
    return separator.join(crumb_links)


print(generate_bc("mysite.com/pictures/holidays?html"))
