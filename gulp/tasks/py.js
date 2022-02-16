const {src , dest } = require("gulp");
const path = require("../config/path.js");

const py = py => {
    return(src(path.src.py))
      .pipe(dest(path.dist.py))

  }



  module.exports = py;