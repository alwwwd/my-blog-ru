const {src , dest } = require("gulp");
const path = require("../config/path.js");


const html =  html => {
    return(src(path.src.html))
      
      .pipe(dest(path.dist.html))
  }
  
  
module.exports = html;