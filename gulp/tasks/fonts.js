const {src , dest } = require("gulp");

// const woff2 = require("gulp-ttf2woff2");

// const woff = require("gulp-ttf2woff");
const path = require("../config/path.js");


const fonts = () =>{
    return(src(path.src.fonts))
        .pipe(dest(path.dist.fonts))
        
}



module.exports = fonts;
