const {src , dest } = require("gulp");
const path = require("../config/path.js");


const db = db  => {
    return(src(path.src.db))
      .pipe(dest(path.dist.db))
  }

  module.exports = db;