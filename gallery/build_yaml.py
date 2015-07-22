import yaml
import os


# Pre-crawl "other" directory
others = os.listdir("other")

for scriptname in os.listdir("source"):
    if scriptname[-3:] == ".py":
        example_name = scriptname[:-3]
        example = {
            "layout": "example",
            "script": scriptname,
            "fullsize": "/gallery/fullsize/%s.png" % example_name,
            "thumb": "/gallery/thumbnails/%s.png" % example_name,
            "other": [],
            "title": example_name
        }
        for o in others:
            if o.startswith(example_name):
                example["other"].append({
                    "type": os.path.splitext(o)[1][1:].lower(),
                    "url": "/gallery/other/%s" % o
                })
        f = open("../_examples/" + example_name + ".md", "w")
        f.write("---\n")
        f.write(yaml.dump(example))
        f.write("\n---\n")
