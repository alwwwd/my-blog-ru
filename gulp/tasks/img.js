const {src , dest } = require("gulp");
const min = require("gulp-imagemin");
const webp = require("gulp-webp");
const path = require("../config/path.js");

const img = img => {
    return(src(path.src.img))
    //   .pipe(webp({
          
    //    }))
    //   .pipe(dest(path.dist.img))
      // .pipe(src(path.src.img))
      .pipe(min({
        prograssive:true,
        svgPlugins:[{removeViewBox : false}],
        interlaced:true,
        optimizetionLevel: 7
      }
      ))
      .pipe(dest(path.dist.img))
  }
  
  
module.exports = img;