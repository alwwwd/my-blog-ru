const {src , dest } = require("gulp");
const include = require("gulp-file-include");
const path = require("../config/path.js");


const js= js => {
    return(src(path.src.js))
      .pipe(include())
      .pipe(dest("./dist/static/js/"))
}
  
  
module.exports = js;