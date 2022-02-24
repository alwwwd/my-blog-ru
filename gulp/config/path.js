Path_dist = "./dist"
static = "/static/"
template = "/templates/"
Path_src = "./src"

const path = {
    dist : {
        html:Path_dist + template,
        css: Path_dist + static+ "css/",
        js:  Path_dist + static + "js/",
        fonts: Path_dist + static +"/fonts/",
        img: Path_dist + static + "img/",
        py:  Path_dist,
        db:Path_dist,

    },

    src : {
        html:Path_src + template +"*.html",
        scss:Path_src + static +  "scss/style.scss",
        js: Path_src + static + "js/script.js",
        img:Path_src + static + "img/*.*",
        py: Path_src + "/app.py",
        db: Path_src +"/*.sqlite",
        fonts: Path_src + static +"/fonts/*.ttf"
    },
    watch :{
        html:Path_src + template,
        scss:Path_src + static + "scss/*.scss",
        js:  Path_src + static + "js/*.js",
        py:  Path_src + "*.py",
        img: Path_src + static + "img/*.img",
        fonts:Path_src + static +"/fonts/*.ttf",
        db: Path_src +"/*.sqlite"
    }
}

module.exports = path;